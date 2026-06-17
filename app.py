<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>أنيميا AI – فحص ذكي لفقر الدم</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue:       #2563EB;
      --blue-dark:  #1D4ED8;
      --blue-light: #EFF6FF;
      --blue-mid:   #BFDBFE;
      --navy:       #1E2D4E;
      --text:       #0F172A;
      --text-muted: #64748B;
      --border:     #E2E8F0;
      --bg:         #F0F4FF;
      --white:      #FFFFFF;
      --red:        #EF4444;
      --green:      #16A34A;
      --green-bg:   #F0FDF4;
      --red-bg:     #FEF2F2;
      --radius:     14px;
      --shadow:     0 4px 24px rgba(37,99,235,.10);
      --shadow-lg:  0 8px 40px rgba(37,99,235,.16);
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Cairo', sans-serif;
      color: var(--text);
      background: var(--white);
      overflow-x: hidden;
    }

    /* ─── NAVBAR ─── */
    nav {
      position: sticky; top: 0; z-index: 100;
      background: rgba(255,255,255,.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0 5vw;
      display: flex; align-items: center; justify-content: space-between;
      height: 68px;
    }
    .logo { font-size: 1.45rem; font-weight: 800; color: var(--navy); }
    .logo span { color: var(--blue); }
    nav ul { list-style: none; display: flex; gap: 2.2rem; }
    nav ul a { text-decoration: none; color: var(--text-muted); font-weight: 600; font-size: .97rem; transition: color .2s; }
    nav ul a:hover { color: var(--blue); }
    .btn-nav {
      background: var(--blue); color: var(--white);
      border: none; border-radius: 10px; padding: .55rem 1.3rem;
      font-family: 'Cairo', sans-serif; font-weight: 700; font-size: .95rem;
      cursor: pointer; transition: background .2s, transform .15s;
    }
    .btn-nav:hover { background: var(--blue-dark); transform: translateY(-1px); }

    /* ─── HERO ─── */
    #home {
      min-height: 88vh;
      display: flex; align-items: center; justify-content: center;
      background: linear-gradient(160deg, #EFF6FF 0%, #F8FAFF 55%, #EFF6FF 100%);
      padding: 5rem 5vw 4rem;
      text-align: center;
    }
    .hero-inner { max-width: 720px; }
    .hero-badge {
      display: inline-flex; align-items: center; gap: .5rem;
      background: rgba(37,99,235,.08); border: 1px solid var(--blue-mid);
      color: var(--blue); border-radius: 99px;
      padding: .4rem 1.1rem; font-size: .9rem; font-weight: 700;
      margin-bottom: 1.6rem;
    }
    .hero-badge::before { content: '✦'; font-size: .75rem; }
    h1 { font-size: clamp(2.4rem, 6vw, 3.8rem); font-weight: 900; line-height: 1.18; color: var(--navy); margin-bottom: 1.1rem; }
    h1 span { color: var(--blue); }
    .hero-sub { font-size: 1.08rem; color: var(--text-muted); line-height: 1.8; max-width: 540px; margin: 0 auto 2.4rem; }
    .hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .btn-primary {
      background: var(--blue); color: var(--white);
      padding: .85rem 2rem; border-radius: 12px;
      font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 1rem;
      border: none; cursor: pointer;
      transition: background .2s, transform .15s, box-shadow .2s;
      box-shadow: 0 4px 18px rgba(37,99,235,.35);
    }
    .btn-primary:hover { background: var(--blue-dark); transform: translateY(-2px); box-shadow: var(--shadow-lg); }
    .btn-outline {
      background: var(--white); color: var(--blue);
      padding: .85rem 2rem; border-radius: 12px;
      font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 1rem;
      border: 2px solid var(--blue-mid); cursor: pointer;
      transition: border-color .2s, background .2s;
    }
    .btn-outline:hover { border-color: var(--blue); background: var(--blue-light); }

    /* ─── WHY US ─── */
    #why { padding: 5rem 5vw; background: var(--white); }
    .section-eyebrow { text-align: center; color: var(--blue); font-weight: 700; font-size: .9rem; letter-spacing: .06em; margin-bottom: .6rem; }
    .section-title { text-align: center; font-size: clamp(1.6rem, 3.5vw, 2.4rem); font-weight: 800; color: var(--navy); margin-bottom: .7rem; }
    .section-sub { text-align: center; color: var(--text-muted); font-size: 1rem; max-width: 540px; margin: 0 auto 3rem; line-height: 1.75; }
    .cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; max-width: 1000px; margin: 0 auto; }
    .card { background: var(--blue-light); border: 1px solid var(--blue-mid); border-radius: var(--radius); padding: 1.8rem 1.6rem; transition: box-shadow .2s, transform .2s; }
    .card:hover { box-shadow: var(--shadow); transform: translateY(-3px); }
    .card-icon { width: 52px; height: 52px; border-radius: 12px; background: var(--blue); display: flex; align-items: center; justify-content: center; margin-bottom: 1.1rem; font-size: 1.5rem; }
    .card h3 { font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: .45rem; }
    .card p  { font-size: .93rem; color: var(--text-muted); line-height: 1.7; }

    /* ─── HOW IT WORKS ─── */
    #how { padding: 5rem 5vw; background: linear-gradient(160deg, #F0F4FF 0%, #EFF6FF 100%); }
    .steps { display: flex; flex-direction: column; gap: 1.5rem; max-width: 680px; margin: 0 auto; }
    .step { display: flex; gap: 1.2rem; align-items: flex-start; background: var(--white); border-radius: var(--radius); padding: 1.5rem; border: 1px solid var(--border); box-shadow: var(--shadow); }
    .step-num { min-width: 42px; height: 42px; border-radius: 50%; background: var(--blue); color: var(--white); font-weight: 800; font-size: 1.1rem; display: flex; align-items: center; justify-content: center; }
    .step h4 { font-size: 1rem; font-weight: 700; color: var(--navy); margin-bottom: .3rem; }
    .step p  { font-size: .92rem; color: var(--text-muted); line-height: 1.7; }

    /* ─── CHECKER ─── */
    #checker { padding: 5rem 5vw; background: var(--white); }
    .checker-wrap { max-width: 820px; margin: 0 auto; background: var(--blue-light); border: 1px solid var(--blue-mid); border-radius: 20px; padding: 2.5rem; }
    .checker-title { font-size: 1.4rem; font-weight: 800; color: var(--navy); margin-bottom: .35rem; }
    .checker-desc  { font-size: .95rem; color: var(--text-muted); margin-bottom: 2rem; line-height: 1.7; }

    .form-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
    .field label { display: block; font-size: .88rem; font-weight: 700; color: var(--navy); margin-bottom: .35rem; }
    .field .hint { font-size: .78rem; color: var(--text-muted); margin-bottom: .35rem; }
    .field input, .field select {
      width: 100%; padding: .65rem .9rem;
      border: 1.5px solid var(--border); border-radius: 10px;
      font-family: 'Cairo', sans-serif; font-size: .95rem; color: var(--text);
      background: var(--white); outline: none;
      transition: border-color .2s, box-shadow .2s;
    }
    .field input:focus, .field select:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(37,99,235,.12); }

    .btn-check {
      width: 100%; padding: 1rem; border-radius: 12px;
      background: var(--blue); color: var(--white);
      font-family: 'Cairo', sans-serif; font-weight: 800; font-size: 1.05rem;
      border: none; cursor: pointer;
      transition: background .2s, transform .15s, box-shadow .2s;
      box-shadow: 0 4px 18px rgba(37,99,235,.3);
      margin-top: .5rem;
    }
    .btn-check:hover:not(:disabled) { background: var(--blue-dark); transform: translateY(-1px); }
    .btn-check:disabled { opacity: .65; cursor: not-allowed; }

    /* Result box */
    #result-box { margin-top: 2rem; border-radius: 14px; overflow: hidden; display: none; }
    #result-box.show { display: block; animation: fadeIn .35s ease; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:none; } }

    .result-header { display: flex; align-items: center; gap: 1rem; padding: 1.3rem 1.6rem; }
    .result-icon { font-size: 2rem; }
    .result-label { font-size: .8rem; font-weight: 700; letter-spacing: .05em; opacity: .8; }
    .result-title { font-size: 1.2rem; font-weight: 800; }
    .result-body { padding: 1.4rem 1.6rem; background: rgba(255,255,255,.65); }
    .result-body p { font-size: .97rem; line-height: 1.85; color: var(--text); }

    .result-anemia .result-header  { background: var(--red-bg); color: var(--red); }
    .result-normal .result-header  { background: var(--green-bg); color: var(--green); }
    .result-anemia { border: 1.5px solid #FECACA; border-radius: 14px; }
    .result-normal { border: 1.5px solid #BBF7D0; border-radius: 14px; }

    .prob-bar-wrap { margin-top: 1rem; }
    .prob-bar-wrap label { font-size: .85rem; font-weight: 700; color: var(--text-muted); margin-bottom: .4rem; display: block; }
    .prob-bar { height: 12px; border-radius: 99px; background: var(--border); overflow: hidden; }
    .prob-bar-fill { height: 100%; border-radius: 99px; transition: width .8s cubic-bezier(.4,0,.2,1); }

    /* AI report section */
    .ai-section { margin-top: 1.2rem; border-top: 1px solid var(--border); padding-top: 1.2rem; }
    .ai-label { font-size: .82rem; font-weight: 700; color: var(--blue); margin-bottom: .6rem; display: flex; align-items: center; gap: .4rem; }
    .ai-report { font-size: .95rem; line-height: 1.85; color: var(--text); }
    .ai-loading { display: flex; align-items: center; gap: .7rem; color: var(--text-muted); font-size: .9rem; }

    .disclaimer {
      margin-top: 1.5rem; padding: 1rem 1.2rem;
      background: rgba(37,99,235,.05); border-radius: 10px;
      border: 1px solid var(--blue-mid);
      font-size: .83rem; color: var(--text-muted); line-height: 1.7;
      display: flex; gap: .6rem; align-items: flex-start;
    }
    .disclaimer span { font-size: 1.1rem; margin-top: .05rem; }

    .spinner {
      display: inline-block; width: 18px; height: 18px;
      border: 3px solid rgba(255,255,255,.4);
      border-top-color: var(--white);
      border-radius: 50%; animation: spin .7s linear infinite;
      vertical-align: middle; margin-left: .5rem;
    }
    .spinner-blue {
      display: inline-block; width: 16px; height: 16px;
      border: 2.5px solid var(--blue-mid);
      border-top-color: var(--blue);
      border-radius: 50%; animation: spin .7s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* ─── FOOTER ─── */
    footer { background: var(--navy); color: rgba(255,255,255,.6); text-align: center; padding: 2rem 5vw; font-size: .88rem; line-height: 1.9; }
    footer strong { color: rgba(255,255,255,.9); }
    footer a { color: var(--blue-mid); text-decoration: none; }

    /* Error box */
    .error-box { background: #FEF2F2; border: 1px solid #FECACA; border-radius: 14px; padding: 1.2rem 1.5rem; color: #991B1B; font-size: .95rem; }

    @media (max-width: 600px) {
      nav ul { display: none; }
      .checker-wrap { padding: 1.6rem 1.2rem; }
      .form-grid { grid-template-columns: 1fr 1fr; }
      .hero-btns { flex-direction: column; align-items: center; }
    }
  </style>
</head>
<body>

<!-- ═══ NAVBAR ═══ -->
<nav>
  <div class="logo">Anemia<span>AI</span></div>
  <ul>
    <li><a href="#home">الرئيسية</a></li>
    <li><a href="#how">كيف يعمل؟</a></li>
  </ul>
  <button class="btn-nav" onclick="document.getElementById('checker').scrollIntoView({behavior:'smooth'})">ابدأ الفحص</button>
</nav>

<!-- ═══ HERO ═══ -->
<section id="home">
  <div class="hero-inner">
    <div class="hero-badge">مدعوم بالذكاء الاصطناعي</div>
    <h1>أنيميا <span>AI</span><br>فحص ذكي لفقر الدم</h1>
    <p class="hero-sub">افحص احتمال إصابتك بفقر الدم في ثوانٍ باستخدام الذكاء الاصطناعي — أداة سهلة ومجانية تساعدك على فهم نتائج تحليل دمك (CBC) بشكل مبسط.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="document.getElementById('checker').scrollIntoView({behavior:'smooth'})">ابدأ الفحص الآن ←</button>
      <button class="btn-outline" onclick="document.getElementById('how').scrollIntoView({behavior:'smooth'})">كيف يعمل؟</button>
    </div>
  </div>
</section>

<!-- ═══ WHY US ═══ -->
<section id="why">
  <p class="section-eyebrow">لماذا نحن؟</p>
  <h2 class="section-title">كل ما تحتاجه في مكان واحد</h2>
  <p class="section-sub">نجمع بين دقة الذكاء الاصطناعي وسهولة الاستخدام ليفهم الجميع نتائج تحليل الدم.</p>
  <div class="cards-grid">
    <div class="card"><div class="card-icon">🧠</div><h3>ذكاء اصطناعي متقدم</h3><p>يعتمد النموذج على بيانات CBC حقيقية بدقة تجاوزت 95% في الكشف عن فقر الدم.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>نتائج فورية</h3><p>أدخل قيم تحليلك واحصل على تقييم ذكي ومفصّل خلال ثوانٍ معدودة.</p></div>
    <div class="card"><div class="card-icon">🔒</div><h3>خصوصية تامة</h3><p>لا يتم حفظ أي بيانات شخصية. البيانات لا تُخزَّن بعد انتهاء التحليل.</p></div>
    <div class="card"><div class="card-icon">📊</div><h3>تقرير مفصّل</h3><p>لا مجرد "نعم أو لا" — بل شرح واضح لكل قيمة وتفسير طبي مبسط بالعربية.</p></div>
  </div>
</section>

<!-- ═══ HOW IT WORKS ═══ -->
<section id="how">
  <p class="section-eyebrow">خطوات بسيطة</p>
  <h2 class="section-title">كيف يعمل الفحص الذكي؟</h2>
  <p class="section-sub">ثلاث خطوات فقط وستحصل على تقريرك.</p>
  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div><h4>أدخل قيم CBC الخاصة بك</h4><p>أدخل القيم المتوفرة من تحليل دمك الكامل — يمكنك ترك أي حقل فارغاً إذا لم يكن متاحاً.</p></div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div><h4>يحلل الذكاء الاصطناعي القيم</h4><p>نموذج Random Forest المدرّب يقارن قيمك بآلاف الحالات ويستخلص احتمالية الإصابة.</p></div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div><h4>احصل على تقريرك المفصّل</h4><p>تقرير بالعربية يشرح كل قيمة وما تعنيه، مع توصية واضحة بمراجعة الطبيب إن لزم.</p></div>
    </div>
  </div>
</section>

<!-- ═══ CHECKER ═══ -->
<section id="checker">
  <p class="section-eyebrow">ابدأ الآن</p>
  <h2 class="section-title">فحص فقر الدم الذكي</h2>
  <p class="section-sub">أدخل قيم تحليل دمك وسيقوم الذكاء الاصطناعي بتحليلها فوراً.</p>

  <div class="checker-wrap">
    <h3 class="checker-title">أدخل قيم CBC الخاصة بك</h3>
    <p class="checker-desc">يمكنك إدخال القيم المتوفرة فقط — كلما زادت القيم كانت النتيجة أدق. الحقل الوحيد المطلوب هو الجنس.</p>

    <div class="form-grid">
      <div class="field">
        <label>الجنس <span style="color:var(--red)">*</span></label>
        <select id="f-gender">
          <option value="">-- اختر --</option>
          <option value="F">أنثى</option>
          <option value="M">ذكر</option>
        </select>
      </div>
      <div class="field">
        <label>كريات الدم الحمراء (RBC)</label>
        <div class="hint">مليون/μL · طبيعي: 3.8–5.8</div>
        <input type="number" id="f-rbc" placeholder="مثال: 4.5" step="0.01" min="0" />
      </div>
      <div class="field">
        <label>كريات الدم البيضاء (WBC)</label>
        <div class="hint">ألف/μL · طبيعي: 4–11</div>
        <input type="number" id="f-wbc" placeholder="مثال: 6.5" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>الهيماتوكريت (HCT)</label>
        <div class="hint">% · طبيعي: 36–52</div>
        <input type="number" id="f-hct" placeholder="مثال: 40" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>متوسط حجم كرات الدم (MCV)</label>
        <div class="hint">fL · طبيعي: 80–100</div>
        <input type="number" id="f-mcv" placeholder="مثال: 88" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>متوسط هيموجلوبين الكرة (MCH)</label>
        <div class="hint">pg · طبيعي: 27–34</div>
        <input type="number" id="f-mch" placeholder="مثال: 29" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>تركيز هيموجلوبين الكرة (MCHC)</label>
        <div class="hint">g/dL · طبيعي: 32–36</div>
        <input type="number" id="f-mchc" placeholder="مثال: 33" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>الصفائح الدموية (PLT)</label>
        <div class="hint">ألف/μL · طبيعي: 150–400</div>
        <input type="number" id="f-plt" placeholder="مثال: 250" step="1" min="0" />
      </div>
      <div class="field">
        <label>توزيع حجم كرات الدم (RDW)</label>
        <div class="hint">% · طبيعي: 11.5–14.5</div>
        <input type="number" id="f-rdw" placeholder="مثال: 13" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>متوسط حجم الصفائح (MPV)</label>
        <div class="hint">fL · طبيعي: 7–12</div>
        <input type="number" id="f-mpv" placeholder="مثال: 9" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>النوتروفيل (Neutrophils)</label>
        <div class="hint">% · طبيعي: 50–70</div>
        <input type="number" id="f-neut" placeholder="مثال: 60" step="0.1" min="0" />
      </div>
      <div class="field">
        <label>اللمفاوية (Lymphocyte)</label>
        <div class="hint">% · طبيعي: 20–40</div>
        <input type="number" id="f-lymph" placeholder="مثال: 30" step="0.1" min="0" />
      </div>
    </div>

    <button class="btn-check" id="check-btn" onclick="runCheck()">
      تحليل القيم بالذكاء الاصطناعي
    </button>

    <div id="result-box"></div>

    <div class="disclaimer">
      <span>⚠️</span>
      <div>هذه الأداة للأغراض التثقيفية فقط وليست بديلاً عن الاستشارة الطبية. يرجى مراجعة طبيبك لأي قرار طبي.</div>
    </div>
  </div>
</section>

<!-- ═══ FOOTER ═══ -->
<footer>
  <strong>AnemiaAI</strong> — فحص ذكي لفقر الدم<br>
  مدعوم بالذكاء الاصطناعي · <a href="#home">الرئيسية</a> · <a href="#checker">ابدأ الفحص</a><br>
  <small style="opacity:.5">© 2025 AnemiaAI. للأغراض التثقيفية فقط.</small>
</footer>

<script>
  function getVal(id) {
    const v = document.getElementById(id).value.trim();
    return v === '' ? null : parseFloat(v);
  }

  async function runCheck() {
    const gender = document.getElementById('f-gender').value;
    if (!gender) { alert('الرجاء اختيار الجنس أولاً.'); return; }

    const values = {
      RBC:         getVal('f-rbc'),
      WBC:         getVal('f-wbc'),
      HEMATOCRIT:  getVal('f-hct'),
      MCV:         getVal('f-mcv'),
      MCH:         getVal('f-mch'),
      MCHC:        getVal('f-mchc'),
      PLATELETS:   getVal('f-plt'),
      'RDW-CV':    getVal('f-rdw'),
      MPV:         getVal('f-mpv'),
      Neutrophils: getVal('f-neut'),
      Lymphocyte:  getVal('f-lymph'),
    };

    const provided = Object.values(values).filter(v => v !== null);
    if (provided.length === 0) { alert('الرجاء إدخال قيمة واحدة على الأقل.'); return; }

    const btn = document.getElementById('check-btn');
    const box = document.getElementById('result-box');
    btn.disabled = true;
    btn.innerHTML = 'جاري التحليل <span class="spinner"></span>';
    box.className = '';
    box.style.display = 'none';

    try {
      // Step 1: ML prediction
      const predRes = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gender, ...values })
      });
      const predData = await predRes.json();
      const prob = predData.probability;
      const isAnemia = predData.prediction === 1;
      const barColor = prob >= 60 ? '#EF4444' : prob >= 40 ? '#F59E0B' : '#16A34A';

      // Show initial result immediately
      box.innerHTML = `
        <div class="result-${isAnemia ? 'anemia' : 'normal'}">
          <div class="result-header">
            <div class="result-icon">${isAnemia ? '⚠️' : '✅'}</div>
            <div>
              <div class="result-label">نتيجة الفحص الذكي</div>
              <div class="result-title">${isAnemia ? 'احتمالية وجود فقر الدم' : 'القيم ضمن النطاق الطبيعي'}</div>
            </div>
          </div>
          <div class="result-body">
            <div class="prob-bar-wrap">
              <label>احتمالية فقر الدم: <strong>${prob}%</strong></label>
              <div class="prob-bar">
                <div class="prob-bar-fill" id="bar-fill" style="width:0%; background:${barColor}"></div>
              </div>
            </div>
            <div class="ai-section">
              <div class="ai-label">🤖 التقرير التفسيري بالذكاء الاصطناعي</div>
              <div class="ai-loading"><span class="spinner-blue"></span> جاري توليد التقرير...</div>
            </div>
          </div>
        </div>`;

      box.className = 'show';
      box.style.display = 'block';
      setTimeout(() => { document.getElementById('bar-fill').style.width = prob + '%'; }, 80);
      box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

      // Step 2: AI analysis
      const aiRes = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gender, probability: prob, values })
      });
      const aiData = await aiRes.json();
      const report = aiData.report || 'تعذّر توليد التقرير.';

      // Replace loading with report
      box.querySelector('.ai-loading').outerHTML;
      box.querySelector('.ai-section').innerHTML = `
        <div class="ai-label">🤖 التقرير التفسيري بالذكاء الاصطناعي</div>
        <div class="ai-report">${report.replace(/\n/g, '<br>')}</div>`;

    } catch (e) {
      box.innerHTML = `<div class="error-box">حدث خطأ أثناء الاتصال. تأكد من تشغيل الخادم وأعد المحاولة.<br><small>${e.message}</small></div>`;
      box.className = 'show';
      box.style.display = 'block';
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'تحليل القيم بالذكاء الاصطناعي';
    }
  }
</script>
</body>
</html>
