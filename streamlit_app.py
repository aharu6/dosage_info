import streamlit as st
import pandas as pd
#投与量シュミレーター
#uv run streamlit run streamlit_app.py
#薬剤　ドロップダウン
drug=st.selectbox(
    "薬剤名を選択",
    options=["乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","乾燥スルホ化人免疫グロブリン（献血ベニロン）"],
)

#疾患名　　薬剤ごとに適応する疾患名表示を変更する
#drugで選択した薬剤名ごとに対応する疾患名リストを用意する
match drug:
    case "乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
        disease_options=[
            "無又は低ガンマグロブリン血症",
            "重症感染症における抗生物質との併用",
            "特発性血小板減少性紫斑病",
            "川崎病の急性期",
            "慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の筋力低下の改善",
            "慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の運動機能低下の進行抑制（筋力低下の改善が認められた場合）",
            "天疱瘡（ステロイド剤の効果不十分な場合）",
            "スティーブンス・ジョンソン症候群及び中毒性表皮壊死症（ステロイド剤の効果不十分な場合）",
            "水疱性類天疱瘡（ステロイド剤の効果不十分な場合）",
            "ギラン・バレー症候群（急性増悪期で歩行困難な重症例）",
            "血清IgG2値の低下を伴う、肺炎球菌又はインフルエンザ菌を起炎菌とする急性中耳炎、急性気管支炎又は肺炎の発症抑制（ワクチン接種による予防及び他の適切な治療を行っても十分な効果が得られず、発症を繰り返す場合に限る）",
            "多発性筋炎・皮膚筋炎における筋力低下の改善",
            "全身型重症筋無力症"
            ]
        #疾患名リストをドロップダウンで表示
        disease=st.selectbox("疾患名を選択",options=disease_options)
    case "乾燥スルホ化人免疫グロブリン（献血ベニロン）":
        disease_options=[
            "低又は無ガンマグロブリン血症",
            "重症感染症における抗生物質との併用",
            "特発性血小板減少性紫斑病(他剤が無効で著明な出血傾向があり、外科的処置又は出産等一時的止血管理を必要とする場合)",
            "川崎病の急性期(重症であり、冠動脈障害の発生の危険がある場合)",
            "ギラン・バレー症候群(急性増悪期で歩行困難な重症例)",
            "好酸球性多発血管炎性肉芽腫症における神経障害の改善(ステロイド剤が効果不十分な場合に限る)",
            "慢性炎症性脱髄性多発根神経炎(多巣性運動ニューロパチーを含む)の筋力低下の改善",
            "視神経炎の急性期(ステロイド剤が効果不十分な場合)"
        ]
        disease=st.selectbox("疾患名を選択",options=disease_options)

#タイトルはつけない
#体重の入力
weight=st.number_input(
    "体重(kg)",min_value=0.0,value=0.0,
    help="体重をkg単位で入力してください。小数点以下1桁まで入力可能です。"
)


#薬剤名と疾患名の組み合わせごとに投与量を計算する
#最低量と最高投与量は後で
DOSAGE_FORMULAS={
    #乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン)
    #最低量〜最高量　日付により投与量変更となる場合
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","無又は低ガンマグロブリン血症","min"):
    lambda w:200*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","無又は低ガンマグロブリン血症","max"):
    lambda w:600*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","重症感染症における抗生物質との併用","min"):
    lambda w:2500*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","重症感染症における抗生物質との併用","max"):
    lambda w:5000*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","特発性血小板減少性紫斑病","min"):
    lambda w:200*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","特発性血小板減少性紫斑病","max"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","川崎病の急性期","5days"):
    lambda w:200*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","川崎病の急性期","single"):
    lambda w:2000*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の筋力低下の改善"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の運動機能低下の進行抑制（筋力低下の改善が認められた場合）","single"):
    lambda w:1000*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の運動機能低下の進行抑制（筋力低下の改善が認められた場合）","3weeks"):
    lambda w:500*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","天疱瘡（ステロイド剤の効果不十分な場合）"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","スティーブンス・ジョンソン症候群及び中毒性表皮壊死症（ステロイド剤の効果不十分な場合）"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","水疱性類天疱瘡（ステロイド剤の効果不十分な場合）"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","ギラン・バレー症候群（急性増悪期で歩行困難な重症例）"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","血清IgG2値の低下を伴う、肺炎球菌又はインフルエンザ菌を起炎菌とする急性中耳炎、急性気管支炎又は肺炎の発症抑制","first"):
    lambda w:300*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","血清IgG2値の低下を伴う、肺炎球菌又はインフルエンザ菌を起炎菌とする急性中耳炎、急性気管支炎又は肺炎の発症抑制","secondlater"):
    lambda w:200*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","多発性筋炎・皮膚筋炎における筋力低下の改善"):
    lambda w:400*w,
    ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","全身型重症筋無力症"):
    lambda w:400*w,

    #献血ベニロン
    #最低量〜最高量　日付により投与量変更となる場合
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","低又は無ガンマグロブリン血症","min"):
    lambda w:200*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","低又は無ガンマグロブリン血症","max"):
    lambda w:600*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","重症感染症における抗生物質との併用","min"):
    lambda w:2500*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","重症感染症における抗生物質との併用","max"):
    lambda w:5000*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","特発性血小板減少性紫斑病(他剤が無効で著明な出血傾向があり、外科的処置又は出産等一時的止血管理を必要とする場合)","min"):
    lambda w:200*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","特発性血小板減少性紫斑病(他剤が無効で著明な出血傾向があり、外科的処置又は出産等一時的止血管理を必要とする場合)","max"):
    lambda w:400*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","川崎病の急性期(重症であり、冠動脈障害の発生の危険がある場合)","5days"):
    lambda w:200*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","川崎病の急性期(重症であり、冠動脈障害の発生の危険がある場合)","single"):
    lambda w:1000*w,
    ("乾燥スルホ化人    免疫グロブリン（献血ベニロン）","ギラン・バレー症候群(急性増悪期で歩行困難な重症例)"):
    lambda w:400*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","好酸球性多発血管炎性肉芽腫症における神経障害の改善(ステロイド剤が効果不十分な場合に限る)"):
    lambda w:400*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","慢性炎症性脱髄性多発根神経炎(多巣性運動ニューロパチーを含む)の筋力低下の改善"):
    lambda w:400*w,
    ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","視神経炎の急性期(ステロイド剤が効果不十分な場合)"):
    lambda w:400*w

}

#投与量計算と表示
#薬と疾患名の組み合わせにより表示領域が変更される
if weight >0:
    key= (drug,disease)

    dosage_info={
        #グロベニン　最低量〜最高量幅あり
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","無又は低ガンマグロブリン血症"):
        {"display_type":"range","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","重症感染症における抗生物質との併用"):
        {"display_type":"range","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","特発性血小板減少性紫斑病"): 
        {"display_type":"range","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","川崎病の急性期"): 
        {"display_type":"select","speed":"kawasaki"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の筋力低下の改善"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","慢性炎症性脱髄性多発根神経炎（多巣性運動ニューロパチーを含む）の運動機能低下の進行抑制（筋力低下の改善が認められた場合）"):
        {"display_type":"multiple","speed":"cidp"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","天疱瘡（ステロイド剤の効果不十分な場合）"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","スティーブンス・ジョンソン症候群及び中毒性表皮壊死症（ステロイド剤の効果不十分な場合）"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）","水疱性類天疱瘡（ステロイド剤の効果不十分な場合）"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロベニン（献血グロベニン）","ギラン・バレー症候群（急性増悪期で歩行困難な重症例）"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロベニン（献血グロベニン）","血清IgG2値の低下を伴う、肺炎球菌又はインフルエンザ菌を起炎菌とする急性中耳炎、急性気管支炎又は肺炎の発症抑制"):
        {"display_type":"which_days","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロベニン（献血グロベニン）","多発性筋炎・皮膚筋炎における筋力低下の改善"):
        {"display_type":"single","speed":"common"},
        ("乾燥ポリエチレングリコール処理人免疫グロベニン（献血グロベニン）","全身型重症筋無力症（ステロイド剤又はステロイド剤以外の免疫抑制剤が無効な場合）"):
        {"display_type":"single","speed":"common"},

        #献血ベニロン
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","低又は無ガンマグロブリン血症"):
        {"display_type":"range","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","重症感染症における抗生物質との併用"):
        {"display_type":"range","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","特発性血小板減少性紫斑病"):
        {"display_type":"range","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","川崎病の急性期"):
        {"display_type":"select","speed":"kawasaki"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","ギラン・バレー症候群(急性増悪期で歩行困難な重症例)"):
        {"display_type":"single","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","好酸球性多発血管炎性肉芽腫症における神経障害の改善(ステロイド剤が効果不十分な場合に限る)"):
        {"display_type":"single","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","慢性炎症性脱髄性多発根神経炎(多巣性運動ニューロパチーを含む)の筋力低下の改善"):
        {"display_type":"single","speed":"common"},
        ("乾燥スルホ化人免疫グロブリン（献血ベニロン）","視神経炎の急性期(ステロイド剤が効果不十分な場合)"):
        {"display_type":"single","speed":"common"},

    }

    info=dosage_info.get(key,{
        "display_type":"single","speed":"common"
    })

    if info["display_type"]=="single":
        if drug=="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
            st.write(f"投与量: {DOSAGE_FORMULAS[key](weight)} mg")
        #バイアル数計算
        #献血グロベニンなら　500と2500 と5000mgの瓶がある

            vial_needed={
                "500mg":(DOSAGE_FORMULAS[key](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key](weight))//5000
            }
            #表形式
            df =pd.DataFrame([{
                "500mg":f"{vial_needed['500mg']} 瓶",
                "2500mg":f"{vial_needed['2500mg']} 瓶",
                "5000mg":f"{vial_needed['5000mg']} 瓶"
            }])
            st.dataframe(df)
        elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
            st.write(f"投与量: {DOSAGE_FORMULAS[key](weight)} mg")
            vial_needed={
                "500mg":(DOSAGE_FORMULAS[key](weight))//500,
                "1000mg":(DOSAGE_FORMULAS[key](weight))//1000,
                "2500mg":(DOSAGE_FORMULAS[key](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key](weight))//5000
            }
            df =pd.DataFrame([{
                "500mg":f"{vial_needed['500mg']} 瓶",
                "1000mg":f"{vial_needed['1000mg']} 瓶",
                "2500mg":f"{vial_needed['2500mg']} 瓶",
                "5000mg":f"{vial_needed['5000mg']} 瓶"
            }])
            st.dataframe(df)
    elif info["display_type"]=="range":

        if drug=="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
            st.write(f"投与量: {DOSAGE_FORMULAS[key + ('min',)](weight)} mg 〜 {DOSAGE_FORMULAS[key + ('max',)](weight)} mg")
            vial_needed_min={
                "500mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//5000
            }
            vial_needed_max={
                "500mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//5000
            }
            df=pd.DataFrame([
                {"500mg":f"{vial_needed_min['500mg']} 〜 {vial_needed_max['500mg']} 瓶",
                "2500mg":f"{vial_needed_min['2500mg']} 〜 {vial_needed_max['2500mg']} 瓶",
                "5000mg":f"{vial_needed_min['5000mg']} 〜 {vial_needed_max['5000mg']} 瓶"
                }])

            st.dataframe(df)
        elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
            st.write(f"投与量: {DOSAGE_FORMULAS[key + ('min',)](weight)} mg 〜 {DOSAGE_FORMULAS[key + ('max',)](weight)} mg")
            vial_needed_min={
                "500mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//500,
                "1000mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//1000,
                "2500mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('min',)](weight))//5000
            }
            vial_needed_max={
                "500mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//500,
                "1000mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//1000,
                "2500mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('max',)](weight))//5000
            }
            df=pd.DataFrame([
                {"500mg":f"{vial_needed_min['500mg']} 〜 {vial_needed_max['500mg']} 瓶",
                "1000mg":f"{vial_needed_min['1000mg']} 〜 {vial_needed_max['1000mg']} 瓶",
                "2500mg":f"{vial_needed_min['2500mg']} 〜 {vial_needed_max['2500mg']} 瓶",
                "5000mg":f"{vial_needed_min['5000mg']} 〜 {vial_needed_max['5000mg']} 瓶"
                }
            ])
            st.dataframe(df)

    elif info["display_type"]=="multiple":

        if drug =="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
            st.write(f"1日を3週間間隔: {DOSAGE_FORMULAS[key+('single')](weight)} mg")
            vial_needed={
                "500mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//5000
            }
            df1=pd.DataFrame([{
                "500mg":f"{vial_needed['500mg']} 瓶",
                "2500mg":f"{vial_needed['2500mg']} 瓶",
                "5000mg":f"{vial_needed['5000mg']} 瓶"
            }])
            st.dataframe(df1)
            
            st.write(f"2日間連続を3週間間隔:{DOSAGE_FORMULAS[key+('3weeks')](weight)} mg")
            vial_needed={
                "500mg":(DOSAGE_FORMULAS[key + ('3weeks',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('3weeks',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('3weeks',)](weight))//5000
            }
            df2=pd.DataFrame([{
                "500mg":f"{vial_needed['500mg']} 瓶",
                "2500mg":f"{vial_needed['2500mg']} 瓶",
                "5000mg":f"{vial_needed['5000mg']} 瓶"
            }])
            st.dataframe(df2)
        elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
            st.write("現在、該当する疾患と投与方法の組み合わせはありません。")
    elif info["display_type"]=="which_days":
        if drug =="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
            st.write(f"初回投与量: {DOSAGE_FORMULAS[key + ('first',)](weight)} mg")

            vial_needed_first={
                "500mg":(DOSAGE_FORMULAS[key + ('first',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('first',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('first',)](weight))//5000
            }
            df1=pd.DataFrame([{
                "500mg":f"{vial_needed_first['500mg']} 瓶",
                "2500mg":f"{vial_needed_first['2500mg']} 瓶",
                "5000mg":f"{vial_needed_first['5000mg']} 瓶"
            }])
            st.dataframe(df1)

            st.write(f"2回目以降の投与量: {DOSAGE_FORMULAS[key + ('secondlater',)](weight)} mg")
            vial_needed_later={
                "500mg":(DOSAGE_FORMULAS[key + ('secondlater',)](weight))//500,
                "2500mg":(DOSAGE_FORMULAS[key + ('secondlater',)](weight))//2500,
                "5000mg":(DOSAGE_FORMULAS[key + ('secondlater',)](weight))//5000    
            }
            df2=pd.DataFrame([{
                "500mg":f"{vial_needed_later['500mg']} 瓶",
                "2500mg":f"{vial_needed_later['2500mg']} 瓶",
                "5000mg":f"{vial_needed_later['5000mg']} 瓶"
            }])
            st.dataframe(df2)
        elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
            st.write("現在、該当する疾患と投与方法の組み合わせはありません。")

    elif info["display_type"]=="select":
        if drug =="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":
            option=st.selectbox("投与方法を選択",options=["5日間連続投与","1日単回投与"])
            match option:
                case "5日間連続投与":
                    st.write(f"投与量: {DOSAGE_FORMULAS[key + ('5days',)](weight)} mg")
                    vial_needed={
                        "500mg":(DOSAGE_FORMULAS[key + ('5days',)](weight))//500,
                        "2500mg":(DOSAGE_FORMULAS[key + ('5days',)](weight))//2500,
                        "5000mg":(DOSAGE_FORMULAS[key + ('5days',)](weight))//5000
                    }
                    df=pd.DataFrame([{
                        "500mg":f"{vial_needed['500mg']} 瓶",
                        "2500mg":f"{vial_needed['2500mg']} 瓶",
                        "5000mg":f"{vial_needed['5000mg']} 瓶"
                    }])
                    st.dataframe(df)
                case "1日単回投与":
                    st.write(f"投与量: {DOSAGE_FORMULAS[key + ('single',)](weight)} mg")
                    vial_needed={
                        "500mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//500,
                        "2500mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//2500,
                        "5000mg":(DOSAGE_FORMULAS[key + ('single',)](weight))//5000
                    }
                    df=pd.DataFrame([{
                        "500mg":f"{vial_needed['500mg']} 瓶",
                        "2500mg":f"{vial_needed['2500mg']} 瓶",
                        "5000mg":f"{vial_needed['5000mg']} 瓶"
                    }])
                    st.dataframe(df)
        elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
            st.write("現在、該当する疾患と投与方法の組み合わせはありません。")


    #投与スピード
    if drug=="乾燥ポリエチレングリコール処理人免疫グロブリン（献血グロベニン）":

        if info["speed"]=="common":
            #スライダー
            infusion_speed = st.slider("投与速度(mL/kg/分)",min_value=0.00,max_value=0.06,step=0.001)
            speed_per_weight = infusion_speed * weight
            st.write(f"投与速度: {speed_per_weight} mL/分")
            speed_per_hr = speed_per_weight * 60
            st.write(f"投与速度: {speed_per_hr} mL/時")
            #投与速度あたりに使用される薬物量
            #50mg/ml
            drug_amount=50*speed_per_weight
            st.write(f"投与速度あたりの薬物量: {drug_amount} mg/分")
        elif info["speed"]=="kawasaki":
            infusion_speed = st.slider("投与速度(mL/kg/分)",min_value=0.00,max_value=0.06,step=0.001)
            speed_per_weight = infusion_speed * weight
            
            st.write(f"投与速度: {speed_per_weight} mL/分")
            speed_per_hr = speed_per_weight * 60
            st.write(f"投与速度: {speed_per_hr} mL/時")
            #投与速度あたりに使用される薬物量
            drug_amount=50*speed_per_weight
            st.write(f"投与速度あたりの薬物量: {drug_amount} mg/分")
            #12時間以上かけて投与しなければならない
            #最低ml/分の速度

    elif drug=="乾燥スルホ化人免疫グロブリン（献血ベニロン）":
        if info["speed"]=="common":
            infusion_speed = st.slider("投与速度(mL/kg/分)",min_value=0.00,max_value=0.06,step=0.001)
            speed_per_weight = infusion_speed * weight
            st.write(f"投与速度: {speed_per_weight} mL/分")
            speed_per_hr = speed_per_weight * 60
            st.write(f"投与速度: {speed_per_hr} mL/時")
            #投与速度あたりに使用される薬物量
            drug_amount=50*speed_per_weight
            st.write(f"投与速度あたりの薬物量: {drug_amount} mg/分")
        elif info["speed"]=="kawasaki":
            infusion_speed = st.slider("投与速度(mL/kg/分)",min_value=0.00,max_value=0.06,step=0.001)
            speed_per_weight = infusion_speed * weight
            st.write(f"投与速度: {speed_per_weight} mL/分")
            speed_per_hr = speed_per_weight * 60
            st.write(f"投与速度: {speed_per_hr} mL/時")
            #投与速度あたりに使用される薬物量
            drug_amount=50*speed_per_weight
            st.write(f"投与速度あたりの薬物量: {drug_amount} mg/分")
            #12時間以上かけて投与しなければならない
            #最低ml/分の速度