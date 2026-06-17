# AnemiaAI — فحص ذكي لفقر الدم

Flask web app للكشف عن فقر الدم باستخدام نموذج Random Forest + تقرير تفسيري من Claude AI.

---

## 🗂️ هيكل المشروع

```
anemia_app/
├── app.py                        ← Flask backend
├── requirements.txt              ← المكتبات المطلوبة
├── render.yaml                   ← إعدادات النشر على Render
├── model.pkl                     ← نموذج Random Forest المدرّب
├── imputer.pkl                   ← معالج القيم الناقصة
├── cbc_dataset_labeled__2_.csv   ← بيانات التدريب
└── templates/
    └── index.html                ← واجهة المستخدم
```

---

## 🚀 تشغيل محلي

```bash
# 1. إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. تثبيت المكتبات
pip install -r requirements.txt

# 3. تعيين مفتاح Anthropic API
export ANTHROPIC_API_KEY=sk-ant-xxxx   # Mac/Linux
set ANTHROPIC_API_KEY=sk-ant-xxxx      # Windows

# 4. تشغيل التطبيق
python app.py
```

ثم افتح المتصفح على: http://localhost:5000

---

## ☁️ النشر على Render.com

1. ارفع المشروع على GitHub
2. سجّل دخول على [render.com](https://render.com)
3. اضغط **New → Web Service** واختر الـ repo
4. في إعدادات الـ Environment Variables أضف:
   - `ANTHROPIC_API_KEY` = مفتاح Anthropic API الخاص بك
5. اضغط **Deploy** — Render سيقرأ render.yaml تلقائياً

---

## 🔌 API Endpoints

| Endpoint   | Method | وصف                                    |
|------------|--------|----------------------------------------|
| `/`        | GET    | الصفحة الرئيسية                       |
| `/predict` | POST   | تنبؤ ML (JSON: قيم CBC + gender)       |
| `/analyze` | POST   | تقرير AI تفسيري عبر Claude API        |

### مثال `/predict`
```json
POST /predict
{
  "gender": "F",
  "RBC": 3.5,
  "MCV": 72,
  "MCH": 22,
  "MCHC": 30
}
```
```json
{ "probability": 87.3, "prediction": 1 }
```

---

## 📊 النموذج

- **الخوارزمية:** Random Forest (200 شجرة)
- **البيانات:** 1,334 حالة CBC حقيقية من بنغازي
- **الدقة:** ~95% على مجموعة الاختبار
- **الميزات:** RBC, WBC, HEMATOCRIT, MCV, MCH, MCHC, PLATELETS, RDW-CV, MPV, PDW, PCT, Neutrophils, Lymphocyte, Monocyte, Gender
