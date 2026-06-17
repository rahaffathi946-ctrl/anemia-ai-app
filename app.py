import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# ── Feature order (must match training) ──────────────────────────────
FEATURES = ['RBC', 'WBC', 'HEMATOCRIT', 'MCV', 'MCH', 'MCHC',
            'PLATELETS', 'RDW-CV', 'MPV', 'PDW', 'PCT',
            'Neutrophils', 'Lymphocyte', 'Monocyte', 'Gender']

MODEL_PATH   = os.path.join(os.path.dirname(__file__), 'model.pkl')
IMPUTER_PATH = os.path.join(os.path.dirname(__file__), 'imputer.pkl')
DATA_PATH    = os.path.join(os.path.dirname(__file__), 'cbc_dataset_labeled__2_.csv')

# ── Load or train model ───────────────────────────────────────────────
def load_or_train():
    if False:  # always retrain from CSV to avoid pickle version issues
        pass

    print("⏳ Training model...")
    df = pd.read_csv(DATA_PATH, sep=';')
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'].astype(str))

    X = df[FEATURES].copy()
    y = df['Anemia'].copy()

    imputer = SimpleImputer(strategy='median')
    X_imp = pd.DataFrame(imputer.fit_transform(X), columns=FEATURES)

    X_train, X_test, y_train, y_test = train_test_split(
        X_imp, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    joblib.dump(model,   MODEL_PATH)
    joblib.dump(imputer, IMPUTER_PATH)
    print("✅ Model trained and saved")
    return model, imputer

model, imputer = load_or_train()

# ── Normal ranges for context ─────────────────────────────────────────
RANGES = {
    'RBC':        {'label': 'RBC',         'unit': 'مليون/μL',  'F': (3.8, 5.2), 'M': (4.3, 5.8)},
    'WBC':        {'label': 'WBC',         'unit': 'ألف/μL',    'F': (4, 11),    'M': (4, 11)},
    'HEMATOCRIT': {'label': 'HCT',         'unit': '%',          'F': (36, 46),   'M': (40, 52)},
    'MCV':        {'label': 'MCV',         'unit': 'fL',         'F': (80, 100),  'M': (80, 100)},
    'MCH':        {'label': 'MCH',         'unit': 'pg',         'F': (27, 34),   'M': (27, 34)},
    'MCHC':       {'label': 'MCHC',        'unit': 'g/dL',      'F': (32, 36),   'M': (32, 36)},
    'PLATELETS':  {'label': 'PLT',         'unit': 'ألف/μL',    'F': (150, 400), 'M': (150, 400)},
    'RDW-CV':     {'label': 'RDW-CV',      'unit': '%',          'F': (11.5,14.5),'M': (11.5,14.5)},
    'MPV':        {'label': 'MPV',         'unit': 'fL',         'F': (7, 12),    'M': (7, 12)},
    'Neutrophils':{'label': 'Neutrophils', 'unit': '%',          'F': (50, 70),   'M': (50, 70)},
    'Lymphocyte': {'label': 'Lymphocyte',  'unit': '%',          'F': (20, 40),   'M': (20, 40)},
}

def flag_value(feat, val, gender):
    if feat not in RANGES or val is None or np.isnan(val):
        return None
    r = RANGES[feat]
    lo, hi = r[gender]
    if val < lo:
        return f"منخفض ({val} {r['unit']} — الطبيعي: {lo}–{hi})"
    if val > hi:
        return f"مرتفع ({val} {r['unit']} — الطبيعي: {lo}–{hi})"
    return f"طبيعي ({val} {r['unit']})"

def generate_report(gender, prob, values):
    """Generate report without AI - rule-based analysis."""
    lines = []
    low_vals = []
    high_vals = []

    for feat, val in values.items():
        if val is not None:
            flag = flag_value(feat, val, gender)
            if flag:
                label = RANGES.get(feat, {}).get('label', feat)
                lines.append(f"• {label}: {flag}")
                if 'منخفض' in flag:
                    low_vals.append(label)
                elif 'مرتفع' in flag:
                    high_vals.append(label)

    gender_ar = 'أنثى' if gender == 'F' else 'ذكر'
    report_parts = []

    # نتيجة الفحص
    if prob >= 70:
        result = "تشير نتائج الفحص إلى احتمالية مرتفعة للإصابة بفقر الدم."
    elif prob >= 40:
        result = "تشير نتائج الفحص إلى احتمالية متوسطة للإصابة بفقر الدم."
    else:
        result = "تشير نتائج الفحص إلى أن احتمالية فقر الدم منخفضة."
    report_parts.append(result)

    # القيم المنخفضة
    if low_vals:
        report_parts.append(f"القيم المنخفضة تشمل: {', '.join(low_vals)}، وهي مؤشرات مرتبطة بفقر الدم.")

    # القيم المرتفعة
    if high_vals:
        report_parts.append(f"القيم المرتفعة تشمل: {', '.join(high_vals)}.")

    # لا توجد قيم شاذة
    if not low_vals and not high_vals:
        report_parts.append("جميع القيم المُدخلة ضمن النطاق الطبيعي.")

    # التوصية
    if prob >= 60:
        report_parts.append("التوصية: يُنصح بمراجعة الطبيب لإجراء فحوصات إضافية وتأكيد التشخيص.")
    elif prob >= 35:
        report_parts.append("التوصية: يُنصح بالمتابعة وإعادة الفحص خلال فترة قريبة.")
    else:
        report_parts.append("التوصية: النتائج مطمئنة، يُنصح بالمتابعة الدورية للحفاظ على الصحة.")

    return ' '.join(report_parts)

# ══════════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════════

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """ML prediction endpoint — returns probability + class."""
    data = request.get_json()
    gender_str = data.get('gender', 'F')
    gender_num = 1 if gender_str == 'M' else 0

    row = []
    for feat in FEATURES:
        if feat == 'Gender':
            row.append(gender_num)
        else:
            v = data.get(feat)
            row.append(float(v) if v not in (None, '', 'null') else np.nan)

    X = pd.DataFrame([row], columns=FEATURES)
    X_imp = pd.DataFrame(imputer.transform(X), columns=FEATURES)

    prob = float(model.predict_proba(X_imp)[0][1])
    pred = int(model.predict(X_imp)[0])

    return jsonify({'probability': round(prob * 100, 1), 'prediction': pred})


@app.route('/analyze', methods=['POST'])
def analyze():
    """Rule-based analysis — no external API needed."""
    data   = request.get_json()
    gender = data.get('gender', 'F')
    prob   = data.get('probability', 50)
    values = data.get('values', {})

    report = generate_report(gender, prob, values)
    return jsonify({'report': report})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
