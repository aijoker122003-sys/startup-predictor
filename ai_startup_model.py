# ai_startup_model.py
import streamlit as st
import random
import time
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd

# ------------------------------
# Multi-language Support
# ------------------------------
LANGUAGES = {
    "ar": "العربية 🇸🇦",
    "en": "English 🇺🇸", 
    "zh": "中文 🇨🇳",
    "de": "Deutsch 🇩🇪",
    "it": "Italiano 🇮🇹"
}

TEXTS = {
    "ar": {
        "title": "🚀 محلل المشاريع الناشئة المتقدم",
        "subtitle": "المنصة الذكية لتحليل فرص نجاح المشاريع الناشئة",
        "project_name": "اسم المشروع 🏢",
        "project_desc": "وصف المشروع 📄",
        "current_price": "السعر الحالي ($) 💵",
        "category": "الفئة / الصناعة 🏷",
        "investment": "الاستثمار المخطط ($) 💼",
        "team_size": "حجم الفريق",
        "analyze_btn": "🚀 تحليل المشروع المتقدم",
        "analyzing": "🔮 جاري تحليل مشروعك باستخدام الذكاء الاصطناعي...",
        "results": "📊 نتائج التحليل المتقدم",
        "success_prob": "احتمالية النجاح",
        "suggested_country": "الدولة المقترحة",
        "suggested_price": "السعر المقترح",
        "market_growth": "نمو القطاع",
        "market_analysis": "📈 تحليل السوق",
        "risk_assessment": "⚠ تقييم المخاطر",
        "desc_analysis": "📝 تحليل الوصف",
        "next_steps": "👣 الخطوات التالية",
        "recommendations": "💡 التوصيات الذكية",
        "success_gauge": "📊 تصور احتمالية النجاح",
        "footer_note": "🛡 ملاحظة: هذا التحليل لأغراض استشارية ويعتمد على نماذج إحصائية متقدمة",
        "categories": ["تكنولوجيا", "العناية بالبشرة", "اللياقة", "التعليم", "الطعام", "أخرى"],
        "market_size": "حجم السوق",
        "competition": "مستوى المنافسة",
        "growth_rate": "معدل النمو",
        "word_count": "عدد الكلمات",
        "sentence_count": "عدد الجمل", 
        "avg_sentence": "متوسط طول الجمل",
        "from_current": "عن السعر الحالي"
    },
    "en": {
        "title": "🚀 Advanced Startup Predictor Pro",
        "subtitle": "The Intelligent Platform for Startup Success Analysis",
        "project_name": "Project Name 🏢",
        "project_desc": "Project Description 📄",
        "current_price": "Current Price ($) 💵",
        "category": "Category / Industry 🏷",
        "investment": "Planned Investment ($) 💼",
        "team_size": "Team Size",
        "analyze_btn": "🚀 Analyze Project Advanced",
        "analyzing": "🔮 Analyzing your project with AI...",
        "results": "📊 Advanced Analysis Results",
        "success_prob": "Success Probability",
        "suggested_country": "Suggested Country",
        "suggested_price": "Suggested Price", 
        "market_growth": "Market Growth",
        "market_analysis": "📈 Market Analysis",
        "risk_assessment": "⚠ Risk Assessment",
        "desc_analysis": "📝 Description Analysis",
        "next_steps": "👣 Next Steps",
        "recommendations": "💡 Smart Recommendations",
        "success_gauge": "📊 Success Probability Visualization",
        "footer_note": "🛡 Note: This analysis is for advisory purposes and uses advanced statistical models",
        "categories": ["Tech", "Skincare", "Fitness", "Education", "Food", "Other"],
        "market_size": "Market Size",
        "competition": "Competition Level",
        "growth_rate": "Growth Rate",
        "word_count": "Word Count",
        "sentence_count": "Sentence Count",
        "avg_sentence": "Avg. Sentence Length",
        "from_current": "from current price"
    },
    "zh": {
        "title": "🚀 高级初创企业预测专家",
        "subtitle": "智能初创企业成功分析平台",
        "project_name": "项目名称 🏢",
        "project_desc": "项目描述 📄",
        "current_price": "当前价格 ($) 💵",
        "category": "类别 / 行业 🏷",
        "investment": "计划投资 ($) 💼",
        "team_size": "团队规模",
        "analyze_btn": "🚀 高级项目分析",
        "analyzing": "🔮 正在使用AI分析您的项目...",
        "results": "📊 高级分析结果",
        "success_prob": "成功概率",
        "suggested_country": "建议国家",
        "suggested_price": "建议价格",
        "market_growth": "市场增长",
        "market_analysis": "📈 市场分析",
        "risk_assessment": "⚠ 风险评估",
        "desc_analysis": "📝 描述分析",
        "next_steps": "👣 后续步骤",
        "recommendations": "💡 智能建议",
        "success_gauge": "📊 成功概率可视化",
        "footer_note": "🛡 注意：此分析仅供参考，使用高级统计模型",
        "categories": ["科技", "护肤", "健身", "教育", "食品", "其他"],
        "market_size": "市场规模",
        "competition": "竞争水平",
        "growth_rate": "增长率",
        "word_count": "字数",
        "sentence_count": "句子数",
        "avg_sentence": "平均句长",
        "from_current": "相对于当前价格"
    },
    "de": {
        "title": "🚀 Erweiterter Startup-Prognose-Profi",
        "subtitle": "Die intelligente Plattform für Startup-Erfolgsanalyse",
        "project_name": "Projektname 🏢",
        "project_desc": "Projektbeschreibung 📄",
        "current_price": "Aktueller Preis ($) 💵",
        "category": "Kategorie / Branche 🏷",
        "investment": "Geplante Investition ($) 💼",
        "team_size": "Teamgröße",
        "analyze_btn": "🚀 Erweiterte Projektanalyse",
        "analyzing": "🔮 Analysiere Ihr Projekt mit KI...",
        "results": "📊 Erweiterte Analyseergebnisse",
        "success_prob": "Erfolgswahrscheinlichkeit",
        "suggested_country": "Vorgeschlagenes Land",
        "suggested_price": "Vorgeschlagener Preis",
        "market_growth": "Marktwachstum",
        "market_analysis": "📈 Marktanalyse",
        "risk_assessment": "⚠ Risikobewertung",
        "desc_analysis": "📝 Beschreibungsanalyse",
        "next_steps": "👣 Nächste Schritte",
        "recommendations": "💡 Intelligente Empfehlungen",
        "success_gauge": "📊 Visualisierung der Erfolgswahrscheinlichkeit",
        "footer_note": "🛡 Hinweis: Diese Analyse dient Beratungszwecken und verwendet erweiterte statistische Modelle",
        "categories": ["Technologie", "Hautpflege", "Fitness", "Bildung", "Lebensmittel", "Andere"],
        "market_size": "Marktgröße",
        "competition": "Wettbewerbsniveau",
        "growth_rate": "Wachstumsrate",
        "word_count": "Wortanzahl",
        "sentence_count": "Satzanzahl",
        "avg_sentence": "Durchs. Satzlänge",
        "from_current": "vom aktuellen Preis"
    },
    "it": {
        "title": "🚀 Predittore Avanzato per Startup Pro",
        "subtitle": "La piattaforma intelligente per l'analisi del successo delle startup",
        "project_name": "Nome Progetto 🏢",
        "project_desc": "Descrizione Progetto 📄",
        "current_price": "Prezzo Attuale ($) 💵",
        "category": "Categoria / Settore 🏷",
        "investment": "Investimento Pianificato ($) 💼",
        "team_size": "Dimensione Team",
        "analyze_btn": "🚀 Analisi Progetto Avanzata",
        "analyzing": "🔮 Analisi del tuo progetto con AI...",
        "results": "📊 Risultati Analisi Avanzata",
        "success_prob": "Probabilità di Successo",
        "suggested_country": "Paese Suggerito",
        "suggested_price": "Prezzo Suggerito",
        "market_growth": "Crescita Mercato",
        "market_analysis": "📈 Analisi Mercato",
        "risk_assessment": "⚠ Valutazione Rischio",
        "desc_analysis": "📝 Analisi Descrizione",
        "next_steps": "👣 Prossimi Passi",
        "recommendations": "💡 Raccomandazioni Intelligenti",
        "success_gauge": "📊 Visualizzazione Probabilità Successo",
        "footer_note": "🛡 Nota: Questa analisi è a scopo consultivo e utilizza modelli statistici avanzati",
        "categories": ["Tecnologia", "Cura della Pelle", "Fitness", "Educazione", "Cibo", "Altro"],
        "market_size": "Dimensione Mercato",
        "competition": "Livello Competizione",
        "growth_rate": "Tasso Crescita",
        "word_count": "Conteggio Parole",
        "sentence_count": "Conteggio Frasi",
        "avg_sentence": "Lung. Media Frase",
        "from_current": "dal prezzo attuale"
    }
}

# ------------------------------
# Enhanced Prediction Function
# ------------------------------
class StartupPredictor:
    def __init__(self, language="en"):
        self.language = language
        self.category_data = {
            "Tech": {"factor": 0.95, "growth": 25, "competition": "High", "countries": ["USA", "Germany", "Israel", "Singapore"]},
            "Skincare": {"factor": 0.85, "growth": 18, "competition": "Medium", "countries": ["France", "South Korea", "USA", "Japan"]},
            "Fitness": {"factor": 0.9, "growth": 22, "competition": "Medium", "countries": ["USA", "Australia", "Germany", "Canada"]},
            "Education": {"factor": 0.87, "growth": 15, "competition": "Medium", "countries": ["USA", "UK", "Canada", "Australia"]},
            "Food": {"factor": 0.8, "growth": 12, "competition": "High", "countries": ["USA", "UK", "Germany", "Japan"]},
            "Other": {"factor": 0.8, "growth": 10, "competition": "Low", "countries": ["USA", "UK", "Germany", "UAE"]}
        }
        
        # Category mapping for different languages
        self.category_mapping = {
            "en": ["Tech", "Skincare", "Fitness", "Education", "Food", "Other"],
            "ar": ["تكنولوجيا", "العناية بالبشرة", "اللياقة", "التعليم", "الطعام", "أخرى"],
            "zh": ["科技", "护肤", "健身", "教育", "食品", "其他"],
            "de": ["Technologie", "Hautpflege", "Fitness", "Bildung", "Lebensmittel", "Andere"],
            "it": ["Tecnologia", "Cura della Pelle", "Fitness", "Educazione", "Cibo", "Altro"]
        }
    
    def set_language(self, language):
        self.language = language
    
    def get_category_key(self, display_category):
        """Convert displayed category to internal key"""
        mapping = self.category_mapping.get(self.language, self.category_mapping["en"])
        if display_category in mapping:
            index = mapping.index(display_category)
            return self.category_mapping["en"][index]
        return "Other"
    
    def analyze_description(self, text):
        """تحليل متقدم للوصف"""
        words = text.split()
        sentences = text.split('.')
        
        return {
            "word_count": len(words),
            "sentence_count": len([s for s in sentences if len(s.strip()) > 0]),
            "avg_sentence_length": len(words) / max(1, len(sentences)),
            "has_numbers": any(char.isdigit() for char in text),
            "has_special_chars": any(not char.isalnum() for char in text)
        }
    
    def predict_success(self, details, category, price, team_size=1):
        """تنبؤ متقدم بنجاح المشروع"""
        if not details or price <= 0:
            return self._default_response()
        
        # Convert category to internal key
        category_key = self.get_category_key(category)
        
        # تحليل الوصف
        desc_analysis = self.analyze_description(details)
        cat_info = self.category_data.get(category_key, self.category_data["Other"])
        
        # حساب النقاط
        desc_score = min(1.0, desc_analysis["word_count"] / 200)
        clarity_score = 0.7 if desc_analysis["avg_sentence_length"] < 25 else 0.4
        detail_score = 0.8 if desc_analysis["word_count"] > 50 else 0.3
        
        # عوامل متقدمة
        team_factor = min(1.2, 1.0 + (team_size - 1) * 0.1)
        growth_factor = 1.0 + (cat_info["growth"] / 100)
        
        # حساب الاحتمالية النهائية
        base_success = 0.4 + (desc_score * 0.3) + (clarity_score * 0.2) + (detail_score * 0.1)
        success_prob = base_success * cat_info["factor"] * growth_factor * team_factor
        
        # تطبيق حدود
        success_prob = max(0.05, min(success_prob, 0.95))
        
        # اقتراح السعر
        suggested_price = self._suggest_price(price, category_key, success_prob)
        
        # اقتراح الدولة
        suggested_country = self._suggest_country(category_key, price)
        
        # التوصيات
        recommendations = self._generate_recommendations(
            success_prob, category_key, desc_analysis, price, suggested_price
        )
        
        return {
            "success_probability": round(success_prob * 100, 2),
            "suggested_country": suggested_country,
            "suggested_price": suggested_price,
            "market_analysis": {
                "category_growth": f"{cat_info['growth']}%",
                "competition_level": cat_info["competition"],
                "market_size": self._get_market_size(category_key)
            },
            "description_analysis": desc_analysis,
            "recommendations": recommendations,
            "risk_factors": self._assess_risks(category_key, price, desc_analysis),
            "next_steps": self._suggest_next_steps(success_prob)
        }
    
    def _suggest_price(self, current_price, category, success_prob):
        """اقتراح سعر متقدم"""
        category_multipliers = {
            "Tech": 1.2, "Skincare": 1.1, "Fitness": 0.9, 
            "Education": 0.8, "Food": 0.95, "Other": 1.0
        }
        
        base_multiplier = category_multipliers.get(category, 1.0)
        success_adjustment = 1.0 + (success_prob - 0.5) * 0.3
        
        suggested = current_price * base_multiplier * success_adjustment
        return max(1.0, round(suggested * (1 + random.uniform(-0.08, 0.12)), 2))
    
    def _suggest_country(self, category, price):
        """اقتراح دولة مع ذكاء أعلى"""
        country_strategies = {
            "Tech": ["USA", "Germany", "Israel", "Singapore", "India"],
            "Skincare": ["South Korea", "France", "Japan", "USA", "Brazil"],
            "Fitness": ["USA", "Australia", "Germany", "Canada", "UK"],
            "Education": ["USA", "UK", "Canada", "Australia", "Germany"],
            "Food": ["USA", "UK", "Germany", "Japan", "UAE"],
            "Other": ["USA", "UK", "Germany", "UAE", "Singapore"]
        }
        
        countries = country_strategies.get(category, ["USA", "UK", "Germany"])
        
        # اختيار استراتيجي بناءً على السعر
        if price < 10:
            return countries[3] if len(countries) > 3 else countries[0]  # أسواق ناشئة
        elif price < 50:
            return countries[1] if len(countries) > 1 else countries[0]  # أسواق متوسطة
        else:
            return countries[0]  # أسواق premium
    
    def _generate_recommendations(self, success_prob, category, desc_analysis, current_price, suggested_price):
        """توليد توصيات مخصصة"""
        recs = []
        
        # توصيات بناءً على الاحتمالية
        if success_prob < 0.3:
            recs.extend([
                "🔍 Conduct deeper market research",
                "🔄 Refine your business idea", 
                "🎯 Focus on a smaller target segment"
            ])
        elif success_prob < 0.6:
            recs.extend([
                "📊 Test your idea with potential customers",
                "💰 Seek initial funding",
                "👥 Build a specialized team"
            ])
        else:
            recs.extend([
                "🚀 Start actual development",
                "📈 Plan marketing campaign",
                "🤝 Look for strategic partners"
            ])
        
        # توصيات بناءً على الوصف
        if desc_analysis["word_count"] < 50:
            recs.append("📝 Develop more detailed product description")
        
        if desc_analysis["avg_sentence_length"] > 25:
            recs.append("✂ Simplify description language")
        
        # توصيات بناءً على السعر
        price_diff = ((suggested_price - current_price) / current_price) * 100
        if abs(price_diff) > 20:
            recs.append(f"💰 Review pricing strategy ({price_diff:+.1f}%)")
        
        return recs
    
    def _assess_risks(self, category, price, desc_analysis):
        """تقييم المخاطر"""
        risks = []
        
        if category in ["Tech", "Food"]:
            risks.append("High market competition")
        
        if price > 100:
            risks.append("High price may limit customer base")
        elif price < 5:
            risks.append("Low profit margin")
        
        if desc_analysis["word_count"] < 30:
            risks.append("Insufficient product description")
        
        return risks if risks else ["Medium risks - manageable"]
    
    def _suggest_next_steps(self, success_prob):
        """اقتراح خطوات تالية"""
        if success_prob < 0.4:
            return [
                "Conduct feasibility study",
                "Analyze competitors",
                "Develop prototype"
            ]
        elif success_prob < 0.7:
            return [
                "Build prototype",
                "Market testing", 
                "Develop business plan"
            ]
        else:
            return [
                "Company registration",
                "Start full development",
                "Launch planning"
            ]
    
    def _get_market_size(self, category):
        """تقدير حجم السوق"""
        sizes = {
            "Tech": "Very Large (500+ billion)",
            "Food": "Large (300+ billion)",
            "Skincare": "Medium (200+ billion)",
            "Fitness": "Medium (150+ billion)", 
            "Education": "Large (400+ billion)",
            "Other": "Diverse"
        }
        return sizes.get(category, "Not specified")
    
    def _default_response(self):
        """رد افتراضي عند وجود أخطاء"""
        return {
            "success_probability": 0.0,
            "suggested_country": "N/A",
            "suggested_price": 0.0,
            "market_analysis": {},
            "description_analysis": {},
            "recommendations": ["Insufficient input data"],
            "risk_factors": ["Incomplete data"],
            "next_steps": ["Complete project data"]
        }

# ------------------------------
# Enhanced Streamlit UI
# ------------------------------
def main():
    st.set_page_config(
        page_title="🚀 Advanced Startup Predictor Pro",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Language selection at the top
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        selected_lang = st.selectbox(
            "🌍 Select Language / اختر اللغة",
            options=list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x],
            index=0
        )
    
    # Get texts for selected language
    t = TEXTS[selected_lang]
    
    # Custom CSS
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #0a0a23 0%, #1a1a40 50%, #4b0082 100%);
        color: #ffffff;
    }}
    
    .main-header {{
        background: linear-gradient(90deg, #6a0dad, #8a2be2);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(106, 13, 173, 0.3);
    }}
    
    .metric-card {{
        background: rgba(26, 26, 46, 0.8);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #6a0dad;
        margin: 0.5rem 0;
        backdrop-filter: blur(10px);
    }}
    
    .recommendation-card {{
        background: rgba(42, 42, 74, 0.9);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border: 1px solid #4b0082;
    }}
    
    .stButton>button {{
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(106, 13, 173, 0.4);
    }}
    
    .success-high {{ color: #00ff88; font-weight: bold; }}
    .success-medium {{ color: #ffaa00; font-weight: bold; }}
    .success-low {{ color: #ff4444; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown(f"""
    <div class="main-header">
        <h1>{t['title']}</h1>
        <p>{t['subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize predictor
    predictor = StartupPredictor(selected_lang)
    
    # Sidebar for additional inputs
    with st.sidebar:
        st.markdown(f"### ⚙ {t['team_size']}")
        team_size = st.slider(t['team_size'], 1, 10, 1, 
                            help="Number of team members")
        
        st.markdown("---")
        st.markdown("### 📊 Market Info")
        st.info("""
        *Note:* 
        This model uses:
        - Market analysis
        - Industry trends  
        - Competitive data
        """)
    
    # Main input form
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Project Information")
        
        project_name = st.text_input(
            t['project_name'],
            placeholder="Enter your innovative project name..."
        )
        
        project_description = st.text_area(
            t['project_desc'],
            placeholder="Describe your project idea in detail... product, team, target market, competitive advantage...",
            height=150
        )
    
    with col2:
        st.markdown("### 💰 Financial Information")
        
        project_price = st.number_input(
            t['current_price'],
            min_value=0.1,
            value=25.0,
            step=5.0,
            help="Proposed price for your product/service"
        )
        
        project_category = st.selectbox(
            t['category'],
            t['categories'],
            help="Choose the category closest to your project"
        )
        
        investment = st.number_input(
            t['investment'],
            min_value=0.0,
            value=10000.0,
            step=1000.0,
            help="Expected investment amount"
        )
    
    # Prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_btn = st.button(
            t['analyze_btn'],
            use_container_width=True,
            type="primary"
        )
    
    if predict_btn:
        if not project_name.strip() or not project_description.strip():
            st.error("❌ Please enter project name and detailed description!")
        elif len(project_description.strip()) < 20:
            st.error("❌ Description should be at least 20 characters!")
        else:
            with st.spinner(t['analyzing']):
                time.sleep(2)
                
                result = predictor.predict_success(
                    project_description.strip(),
                    project_category,
                    project_price,
                    team_size
                )
                
                # Display results
                st.markdown("---")
                st.markdown(f"## {t['results']}")
                
                # Key Metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    success_class = "success-high" if result["success_probability"] > 70 else \
                                  "success-medium" if result["success_probability"] > 40 else "success-low"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{t['success_prob']}</h3>
                        <h2 class="{success_class}">{result['success_probability']}%</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{t['suggested_country']}</h3>
                        <h2>🇺🇸 {result['suggested_country']}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    price_change = ((result['suggested_price'] - project_price) / project_price) * 100
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{t['suggested_price']}</h3>
                        <h2>${result['suggested_price']}</h2>
                        <small>{price_change:+.1f}% {t['from_current']}</small>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{t['market_growth']}</h3>
                        <h2>{result['market_analysis']['category_growth']}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Detailed Analysis
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### {t['market_analysis']}")
                    market_data = {
                        t['market_size']: result['market_analysis']['market_size'],
                        t['competition']: result['market_analysis']['competition_level'],
                        t['growth_rate']: result['market_analysis']['category_growth']
                    }
                    st.dataframe(market_data, use_container_width=True)
                    
                    st.markdown(f"### {t['risk_assessment']}")
                    for risk in result['risk_factors']:
                        st.error(f"• {risk}")
                
                with col2:
                    st.markdown(f"### {t['desc_analysis']}")
                    desc_data = {
                        t['word_count']: result['description_analysis']['word_count'],
                        t['sentence_count']: result['description_analysis']['sentence_count'],
                        t['avg_sentence']: f"{result['description_analysis']['avg_sentence_length']:.1f}"
                    }
                    st.dataframe(desc_data, use_container_width=True)
                    
                    st.markdown(f"### {t['next_steps']}")
                    for step in result['next_steps']:
                        st.info(f"• {step}")
                
                # Recommendations
                st.markdown("---")
                st.markdown(f"### {t['recommendations']}")
                
                for i, recommendation in enumerate(result['recommendations']):
                    st.markdown(f"""
                    <div class="recommendation-card">
                        <strong>Recommendation {i+1}:</strong> {recommendation}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Success Visualization
                st.markdown("---")
                st.markdown(f"### {t['success_gauge']}")
                
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number+delta",
                    value = result['success_probability'],
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Success Indicator"},
                    delta = {'reference': 50},
                    gauge = {
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "#6a0dad"},
                        'steps': [
                            {'range': [0, 30], 'color': "lightgray"},
                            {'range': [30, 70], 'color': "gray"},
                            {'range': [70, 100], 'color': "darkgray"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 90
                        }
                    }
                ))
                
                st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #888;'>
        <p>{t['footer_note']}</p>
        <p>⏰ Last update: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()