import streamlit as st

st.title("🧠 ARCOS Score Calculator")
st.markdown("**Anesthesiology and Risk-based Carotid Operative Stratification**")

# --- Funzione di calcolo dello score ---
def calcola_score(mets, fe, angina, stenosi_aortica, aritmie, nyha,
                  bpco, ventilazione, sat,
                  irc, cirrosi, diabete,
                  reazione_anestesia, intubazione_difficile,
                  tea_precedente, radioterapia, stenosi_distale, stenosi_tandem,
                  paralisi_nervo, nao_tao, occlusione):
    score = (
        mets + fe + angina + stenosi_aortica + aritmie + nyha +
        bpco + ventilazione + sat +
        irc + cirrosi + diabete +
        reazione_anestesia + intubazione_difficile +
        2*tea_precedente + 2*radioterapia + 3*stenosi_distale +
        5*stenosi_tandem + 5*paralisi_nervo + 2*nao_tao + 2*occlusione
    )
    return score

def interpreta(score):
    if score <= 2:
        return "🟢 Rischio BASSO → TEA preferibile"
    elif score <= 4:
        return "🟡 Rischio INTERMEDIO → TEA con cautela o Stenting"
    else:
        return "🔴 Rischio ALTO → Stenting preferibile"

# --- Input utente ---
mets = st.selectbox("Capacità funzionale (METs)", [
    ("≥6 (buona tolleranza)", 0),
    ("4–5 (moderata)", 1),
    ("<4 (scarsa)", 2)
])[1]

fe = st.checkbox("Frazione di eiezione <30%")
angina = st.checkbox("Angina instabile / IMA recente")
stenosi_aortica = st.checkbox("Stenosi aortica severa sintomatica")
aritmie = st.checkbox("Aritmie mal controllate")
nyha = st.checkbox("Classe NYHA III–IV")

bpco = st.checkbox("BPCO severa / ossigenoterapia")
ventilazione = st.checkbox("Ventilazione non invasiva domiciliare")
sat = st.checkbox("Sat <90% in aria ambiente")

irc = st.checkbox("IRC III–IV / dialisi")
cirrosi = st.checkbox("Cirrosi epatica B o C")
diabete = st.checkbox("Diabete con complicanze avanzate")

reazione_anestesia = st.checkbox("Reazione avversa a anestesia")
intubazione_difficile = st.checkbox("Difficile intubazione documentata")

tea_precedente = st.checkbox("Precedente TEA o chirurgia sul collo")
radioterapia = st.checkbox("Precedente radioterapia al collo")
stenosi_distale = st.checkbox("Stenosi carotidea distale")
stenosi_tandem = st.checkbox("Stenosi tandem")
paralisi_nervo = st.checkbox("Paralisi del nervo laringeo controlaterale")
nao_tao = st.checkbox("Terapia NAO/TAO in corso")
occlusione = st.checkbox("Occlusione carotide controlaterale")

# --- Calcolo score ---
if st.button("Calcola Score"):
    score = calcola_score(
        mets, int(fe), int(angina), int(stenosi_aortica), int(aritmie), int(nyha),
        int(bpco), int(ventilazione), int(sat),
        int(irc), int(cirrosi), int(diabete),
        int(reazione_anestesia), int(intubazione_difficile),
        int(tea_precedente), int(radioterapia), int(stenosi_distale),
        int(stenosi_tandem), int(paralisi_nervo), int(nao_tao), int(occlusione)
    )
    st.success(f"Totale: **{score}**")
    st.markdown(f"### {interpreta(score)}")