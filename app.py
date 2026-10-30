#pip install streamlit requests plotly pandas
import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Painel Econômico - PIB Mundial",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Estilização CSS personalizada com negrito e gradientes
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0f4ff 0%, #e6eeff 50%, #f3e8ff 100%);
        color: #0f172a;
        font-weight: 700;
    }

    label[data-testid="stWidgetLabel"] {
        font-weight: 800 !important;
        color: #0f172a !important;
    }

    .gradient-title {
        background: linear-gradient(90deg, #2563eb, #7c3aed, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
        color: white !important;
        font-weight: 800 !important;
        font-size: 1.05rem;
        border-radius: 12px;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5);
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
    }

    .metric-card {
        padding: 1.2rem;
        border-radius: 16px;
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.06);
        margin-bottom: 1rem;
    }

    .card-blue { border-left: 6px solid #3b82f6; background: #eff6ff; }
    .card-purple { border-left: 6px solid #8b5cf6; background: #f5f3ff; }
    .card-green { border-left: 6px solid #10b981; background: #ecfdf5; }
    .card-amber { border-left: 6px solid #f59e0b; background: #fffbeb; }

    .card-title {
        font-size: 0.85rem;
        color: #475569;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .card-value {
        font-size: 1.75rem;
        font-weight: 900;
        color: #0f172a;
        margin-top: 0.2rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Cabeçalho
st.markdown(
    '<h1 class="gradient-title">🌐 Painel Econômico Mundial</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    "**✨ Clique em um país no mapa ou digite o nome para consultar dados de PIB.**"
)

st.divider()

# 4. Estado Inicial da Aplicação
if "pais_selecionado" not in st.session_state:
    st.session_state["pais_selecionado"] = "Brazil"

# 5. Criar Mapa Interativo com Plotly
st.subheader("🗺️ **Selecione o País no Mapa**")

# Dados do mapa-múndi via plotly.express
df_mapa = px.data.gapminder().query("year == 2007")

fig = px.choropleth(
    df_mapa,
    locations="iso_alpha",
    hover_name="country",
    color_discrete_sequence=["#3b82f6"],
    projection="natural earth",
)

fig.update_geos(
    showcountries=True,
    countrycolor="#CBD5E1",
    showcoastlines=True,
    coastlinecolor="#94A3B8",
    showland=True,
    landcolor="#F1F5F9",
    showocean=True,
    oceancolor="#E0F2FE",
    fitbounds="locations",
)

fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=380,
    clickmode="event+select",
    dragmode=False,
)

# Renderizar mapa interativo
map_event = st.plotly_chart(
    fig,
    on_select="rerun",
    selection_mode="points",
    use_container_width=True,
    key="mapa_world",
)

# Detectar clique no mapa
if map_event and map_event.get("selection", {}).get("points"):
    ponto = map_event["selection"]["points"][0]
    if "hovertext" in ponto:
        pais_clicado = ponto["hovertext"]
        if pais_clicado != st.session_state["pais_selecionado"]:
            st.session_state["pais_selecionado"] = pais_clicado
            st.rerun()

st.divider()

# 6. Formulário de Consulta
with st.form("gdp_form"):
    col_country, col_year = st.columns([2, 1])

    with col_country:
        nome = st.text_input(
            "**País (em inglês):**",
            value=st.session_state["pais_selecionado"],
            placeholder="Ex: United States, Japan, Germany",
        )

    with col_year:
        ano = st.text_input("**Ano:**", value="2020", placeholder="Ex: 2021")

    submit_button = st.form_submit_button("🚀 **Consultar PIB**")

API_KEY = "te07gI373afhSRB8I8IdbBErZkYmdzefwwHjCedn"

# 7. Requisição e Exibição dos Resultados
if submit_button:
    if not nome.strip() or not ano.strip():
        st.warning("⚠️ **Por favor, informe o país e o ano desejados.**")
    else:
        with st.spinner("**A carregar informações econômicas...**"):
            try:
                response = requests.get(
                    f"https://api.api-ninjas.com/v1/gdp?country={nome.strip()}&year={ano.strip()}",
                    headers={"X-Api-Key": API_KEY},
                    timeout=30,
                )
                response.raise_for_status()
                dados = response.json()

                if dados:
                    pais = dados[0]

                    st.success("🎉 **Dados recuperados com sucesso!**")
                    st.subheader("📊 **Resultados Obtidos**")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        c_country = pais.get("country", nome.capitalize())
                        st.markdown(
                            f"""
                            <div class="metric-card card-blue">
                                <div class="card-title"><b>🏳️ País</b></div>
                                <div class="card-value"><b>{c_country}</b></div>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    with col2:
                        c_year = pais.get("year", ano)
                        st.markdown(
                            f"""
                            <div class="metric-card card-purple">
                                <div class="card-title"><b>📅 Ano</b></div>
                                <div class="card-value"><b>{c_year}</b></div>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    with col3:
                        growth = pais.get("gdp_growth")
                        growth_val = (
                            f"{growth}%" if growth is not None else "N/A"
                        )
                        st.markdown(
                            f"""
                            <div class="metric-card card-green">
                                <div class="card-title"><b>📈 Crescimento</b></div>
                                <div class="card-value"><b>{growth_val}</b></div>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    if "gdp" in pais:
                        st.markdown(
                            f"""
                            <div class="metric-card card-amber">
                                <div class="card-title"><b>💰 PIB Total</b></div>
                                <div class="card-value"><b>${pais['gdp']:,}</b></div>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    with st.expander("📄 **Ver JSON bruto retornado**"):
                        st.json(pais)

                else:
                    st.error(
                        f"**Nenhum dado encontrado para '{nome}' no ano {ano}.**"
                    )

            except requests.exceptions.HTTPError:
                st.error(
                    f"**Erro na requisição à API (Status {response.status_code}): Verifique a chave de API ou os parâmetros.**"
                )
            except requests.exceptions.RequestException as e:
                st.error(f"**Erro de ligação:** {e}")