import numpy as np
import pandas as pd
import streamlit as st

st.title('Extractor manifold design calculations.')
#Transcribe data tables*************************************************************************************************
f_toList = lambda S:[float(n) for n in S.split(' ')]
#-----------------------------------------------------------------------------------------------------------------------
diffuser_zeta_table = pd.DataFrame({'n_ar':[],'Re':[],'Alpha':[],'Zeta_d':[]})
degrees = [3,4,6,8,10,12,14,16,20,30,45,60,90,120,180]

#Add values for area ratio = 2
n2_row1_table = pd.DataFrame({'n_ar' :[2]*len(degrees),
                              'Re'   :[0.5e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.148,0.135,0.121,0.112,0.107,0.109,0.120,0.141,0.191,0.315,0.331,0.326,0.315,0.308,0.298]})
n2_row2_table = pd.DataFrame({'n_ar' :[2]*len(degrees),
                              'Re'   :[1e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.120,0.106,0.090,0.083,0.080,0.088,0.102,0.122,0.196,0.298,0.297,0.286,0.283,0.279,0.276]})
n2_row3_table = pd.DataFrame({'n_ar' :[2]*len(degrees),
                              'Re'   :[2e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.093,0.082,0.070,0.068,0.062,0.062,0.063,0.073,0.120,0.229,0.279,0.268,0.268,0.265,0.263]})
n2_row4_table = pd.DataFrame({'n_ar' :[2]*len(degrees),
                              'Re'   :[4e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.079,0.068,0.056,0.048,0.048,0.048,0.051,0.051,0.068,0.120,0.271,0.272,0.272,0.268,0.268]})
diffuser_zeta_table = pd.concat([diffuser_zeta_table,n2_row1_table,n2_row2_table,n2_row3_table,n2_row4_table],
                                ignore_index = True)

#Add values for area ratio = 4
n4_row1_table = pd.DataFrame({'n_ar' :[4]*len(degrees),
                              'Re'   :[0.5e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.197,0.180,0.165,0.151,0.157,0.174,0.197,0.225,0.298,0.461,0.606,0.680,0.643,0.630,0.615]})
n4_row2_table = pd.DataFrame({'n_ar' :[4]*len(degrees),
                              'Re'   :[1e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.154,0.141,0.126,0.119,0.120,0.131,0.155,0.183,0.262,0.479,0.680,0.628,0.600,0.593,0.585]})
n4_row3_table = pd.DataFrame({'n_ar' :[4]*len(degrees),
                              'Re'   :[2e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.120,0.112,0.101,0.096,0.096,0.107,0.120,0.146,0.180,0.360,0.548,0.586,0.585,0.580,0.567]})
n4_row4_table = pd.DataFrame({'n_ar' :[4]*len(degrees),
                              'Re'   :[4e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.101,0.091,0.085,0.079,0.082,0.090,0.107,0.124,0.172,0.292,0.462,0.562,0.582,0.577,0.567]})
n4_row5_table = pd.DataFrame({'n_ar' :[4]*len(degrees),
                              'Re'   :[6e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.101,0.091,0.085,0.089,0.080,0.107,0.135,0.169,0.240,0.382,0.506,0.560,0.582,0.577,0.567]})
diffuser_zeta_table = pd.concat([diffuser_zeta_table,n4_row1_table,n4_row2_table,n4_row3_table,n4_row4_table,n4_row5_table],
                                ignore_index = True)

#Add values for area ratio = 6
n6_row1_table = pd.DataFrame({'n_ar' :[6]*len(degrees),
                              'Re'   :[0.5e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.182,0.170,0.168,0.168,0.179,0.200,0.240,0.268,0.330,0.482,0.640,0.766,0.742,0.730,0.722]})
n6_row2_table = pd.DataFrame({'n_ar' :[6]*len(degrees),
                              'Re'   :[1e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.153,0.144,0.131,0.126,0.132,0.159,0.193,0.218,0.286,0.488,0.680,0.755,0.731,0.720,0.707]})
n6_row3_table = pd.DataFrame({'n_ar' :[6]*len(degrees),
                              'Re'   :[2e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.128,0.118,0.109,0.101,0.101,0.118,0.151,0.185,0.280,0.440,0.640,0.700,0.710,0.708,0.690]})
n6_row4_table = pd.DataFrame({'n_ar' :[6]*len(degrees),
                              'Re'   :[4e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':[0.106,0.095,0.090,0.084,0.087,0.104,0.151,0.160,0.224,0.360,0.510,0.660,0.696,0.695,0.680]})
n6_row5_table = pd.DataFrame({'n_ar' :[6]*len(degrees),
                              'Re'   :[6e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.092 0.090 0.080 0.079 0.080 0.098 0.137 0.160 0.286 0.456 0.600 0.690 0.707 0.700 0.695')})

diffuser_zeta_table = pd.concat([diffuser_zeta_table,n6_row1_table,n6_row2_table,n6_row3_table,n6_row4_table,n6_row5_table],
                                ignore_index = True)

#Add values for area ratio = 10
n10_row1_table = pd.DataFrame({'n_ar':[10]*len(degrees),
                              'Re'   :[0.5e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.195 0.181 0.184 0.190 0.220 0.227 0.256 0.290 0.380 0.585 0.760 0.800 0.834 0.840 0.827')})
n10_row2_table = pd.DataFrame({'n_ar':[10]*len(degrees),
                              'Re'   :[1e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.160 0.156 0.155 0.156 0.162 0.184 0.212 0.240 0.332 0.572 0.812 0.800 0.820 0.820 0.815')})
n10_row3_table = pd.DataFrame({'n_ar':[10]*len(degrees),
                              'Re'   :[2e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.123 0.120 0.120 0.123 0.134 0.151 0.167 0.195 0.240 0.426 0.760 0.800 0.806 0.807 0.808')})
n10_row4_table = pd.DataFrame({'n_ar':[10]*len(degrees),
                              'Re'   :[4e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.100 0.097 0.097 0.100 0.106 0.128 0.160 0.195 0.254 0.407 0.605 0.735 0.804 0.805 0.809')})
n10_row5_table = pd.DataFrame({'n_ar':[10]*len(degrees),
                              'Re'   :[6e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.085 0.084 0.084 0.085 0.086 0.114 0.160 0.212 0.332 0.520 0.600 0.760 0.825 0.840 0.825')})
diffuser_zeta_table=pd.concat([diffuser_zeta_table,n10_row1_table,n10_row2_table,n10_row3_table,n10_row4_table,n10_row5_table],
                                ignore_index = True)

#Add values for area ratio = 16
n16_row1_table = pd.DataFrame({'n_ar':[16]*len(degrees),
                              'Re'   :[0.5e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.179 0.174 0.176 0.185 0.196 0.224 0.270 0.306 0.378 0.600 0.840 0.880 0.880 0.880 0.880')})
n16_row2_table = pd.DataFrame({'n_ar':[16]*len(degrees),
                              'Re'   :[1e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.148 0.146 0.147 0.147 0.151 0.179 0.233 0.275 0.340 0.600 0.840 0.905 0.877 0.986 0.876')})
n16_row3_table = pd.DataFrame({'n_ar':[16]*len(degrees),
                              'Re'   :[2e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.118 0.120 0.120 0.120 0.120 0.140 0.176 0.208 0.280 0.520 0.760 0.868 0.868 0.868 0.868')})
n16_row4_table = pd.DataFrame({'n_ar':[16]*len(degrees),
                              'Re'   :[4e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.120 0.098 0.095 0.094 0.095 0.118 0.160 0.191 0.264 0.480 0.700 0.778 0.847 0.868 0.869')})
n16_row5_table = pd.DataFrame({'n_ar':[16]*len(degrees),
                              'Re'   :[6e5]*len(degrees),
                              'Alpha':degrees,
                'Zeta_d':f_toList('0.094 0.085 0.084 0.085 0.094 0.118 0.160 0.212 0.342 0.560 0.720 0.790 0.853 0.874 0.886')})
diffuser_zeta_table=pd.concat([diffuser_zeta_table,n16_row1_table,n16_row2_table,n16_row3_table,n16_row4_table,n16_row5_table],
                                ignore_index = True)
#-----------------------------------------------------------------------------------------------------------------------------------
diffuser_k_table = pd.DataFrame({'n_ar':[],'Re':[],'LD_ratio':[],'Alpha':[],'k_d':[]})
degrees = [3,4,6,8,10,12,14,16,20,30,45,60,90]

#FOR n_ar = 2!-----------------------------------------------------------------------------------------------------------------
#Add values for Re = 0.5e5
Re0_row1_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                              'Re'      :[0.5e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.10 1.20 1.25 1.26 1.26 1.23 1.16 1.05 1.00 0.01 1.01 1.01')})
Re0_row2_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[0.5e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.45 1.62 1.75 1.83 1.86 1.80 1.70 1.53 1.10 1.02 1.02 1.02 1.02')})
Re0_row3_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[0.5e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.88 1.96 2.05 2.07 2.07 2.05 2.00 1.93 1.60 1.12 1.11 1.10 1.10')})
Re0_row4_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[0.5e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.68 1.83 1.96 2.00 1.99 1.93 1.85 1.74 1.45 1.03 1.01 1.01 1.01')})
diffuser_k_table=pd.concat([diffuser_k_table,Re0_row1_table,Re0_row2_table,Re0_row3_table,Re0_row4_table],ignore_index = True)

#Add values for Re = 1e5
Re1_row1_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[1e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.10 1.20 1.27 1.43 1.60 1.67 1.60 1.10 0.85 0.96 1.11 1.13')})
Re1_row2_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[1e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.63 1.83 2.00 2.11 2.20 2.19 2.11 1.88 1.20 1.00 1.13 1.15 1.15')})
Re1_row3_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[1e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.93 2.13 .241 2.75 2.93 3.00 3.05 2.99 1.40 1.100 1.13 1.15 1.15')})
Re1_row4_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[1e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.86 2.07 2.31 2.60 2.68 2.60 2.45 2.13 1.45 1.00 1.13 1.13 1.15')})
diffuser_k_table=pd.concat([diffuser_k_table,Re1_row1_table,Re1_row2_table,Re1_row3_table,Re1_row4_table],ignore_index = True)

#Add values for Re=(2-5)e5, use 2 for matching purpose
Re2_row1_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[2e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.18 1.33 1.50 1.67 1.95 2.20 2.31 2.13 1.60 1.27 1.14 1.13 1.11')})
Re2_row2_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[2e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.15 1.75 2.05 2.30 2.60 2.70 2.80 3.58 1.85 1.33 1.15 1.14 1.11')})
Re2_row3_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[2e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('2.06 2.25 2.54 2.91 3.40 3.70 3.82 3.73 2.27 1.50 1.26 1.20 1.12')})
Re2_row4_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[2e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.75 1.93 2.28 2.60 3.00 3.22 3.36 3.20 2.10 1.43 1.20 1.16 1.11')})
diffuser_k_table=pd.concat([diffuser_k_table,Re2_row1_table,Re2_row2_table,Re2_row3_table,Re2_row4_table],ignore_index = True)

#Add values for Re>6e5, use 10 for matching purpose
Re6_row1_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[10e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.14 1.33 1.65 1.90 2.00 2.06 1.90 1.53 1.26 1.10 1.07 1.10')})
Re6_row2_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[10e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.15 1.33 1.60 1.90 2.06 2.10 1.20 1.90 2.20 1.62 1.30 1.23 1.10')})
Re6_row3_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[10e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.73 1.90 2.15 2.45 2.93 3.13 3.25 3.15 2.20 1.62 1.30 1.23 1.10')})
Re6_row4_table = pd.DataFrame({'n_ar'   :[2]*len(degrees),
                               'Re'      :[10e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.46 1.65 1.95 2.86 2.54 2.65 2.70 2.60 1.70 1.33 1.13 1.12 1.10')})
diffuser_k_table=pd.concat([diffuser_k_table,Re6_row1_table,Re6_row2_table,Re6_row3_table,Re6_row4_table],ignore_index = True)

#FOR n_ar = 4-16!, use 6 for matching purpose---------------------------------------------------------------------------------
#Add values for Re=0.5e5
Re0_row1_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[0.5e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.04 1.07 1.20 1.33 1.28 1.05 1.14 1.07 1.05 1.05 1.06 1.05')})
Re0_row2_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[0.5e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.25 1.47 1.60 1.66 1.65 1.60 1.58 1.43 1.23 1.08 1.06 1.05')})
Re0_row3_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[0.5e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.50 1.65 1.85 1.90 2.10 2.10 2.05 1.93 1.70 1.38 1.26 1.20 1.05')})
Re0_row4_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[0.5e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.30 1.43 1.65 1.85 1.98 1.74 1.75 1.66 1.48 1.23 1.10 1.06 1.05')})
diffuser_k_table=pd.concat([diffuser_k_table,Re0_row1_table,Re0_row2_table,Re0_row3_table,Re0_row4_table],ignore_index = True)
#Add values for Re=1e5
Re1_row1_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[1e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.05 1.10 1.14 1.26 1.47 1.40 1.28 1.18 1.06 0.95 0.95 0.95 1.02')})
Re1_row2_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[1e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.30 1.46 1.68 1.93 2.15 2.15 2.05 1.90 1.60 1.07 1.00 1.00 1.02')})
Re1_row3_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[1e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.67 1.83 2.08 2.28 2.60 2.50 2.43 2.20 1.83 1.30 1.10 1.03 1.02')})
Re1_row4_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[1e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.50 1.63 1.93 2.15 2.60 2.50 2.27 2.07 1.73 1.20 1.05 1.07 1.02')})
diffuser_k_table=pd.concat([diffuser_k_table,Re1_row1_table,Re1_row2_table,Re1_row3_table,Re1_row4_table],ignore_index = True)
#Add values for Re=(2-5)e5, use 2 for matching purpose
Re2_row1_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[2e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.20 1.40 1.63 2.05 2.13 2.07 1.95 1.68 1.32 1.15 1.13 1.07')})
Re2_row2_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[2e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.30 1.47 1.69 2.00 2.27 2.35 2.37 2.27 1.95 1.40 1.19 1.13 1.07')})
Re2_row3_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[2e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.80 2.00 2.25 2.60 3.30 3.20 3.00 2.80 2.40 1.53 1.26 1.20 1.07')})
Re2_row4_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[2e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.54 1.73 2.12 2.43 3.20 3.00 2.75 2.50 2.10 1.50 1.23 1.15 1.07')})
diffuser_k_table=pd.concat([diffuser_k_table,Re2_row1_table,Re2_row2_table,Re2_row3_table,Re2_row4_table],ignore_index = True)
#Add values for Re=6e5, use 10 for matching purpose
Re6_row1_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[10e5]*len(degrees),
                              'LD_ratio':[2]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.00 1.13 1.42 1.73 1.98 1.93 1.83 1.70 1.50 1.23 1.13 1.10 1.07')})
Re6_row2_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[10e5]*len(degrees),
                              'LD_ratio':[5]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.05 1.23 1.60 1.95 2.25 2.20 2.08 1.90 1.55 1.25 1.15 1.10 1.07')})
Re6_row3_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[10e5]*len(degrees),
                              'LD_ratio':[10]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.60 1.82 2.15 2.55 3.20 3.02 2.53 2.20 1.83 1.33 1.22 1.18 1.07')})
Re6_row4_table = pd.DataFrame({'n_ar'   :[6]*len(degrees),
                               'Re'     :[10e5]*len(degrees),
                              'LD_ratio':[20]*len(degrees),
                              'Alpha'   :degrees,
                'k_d':f_toList('1.35 1.63 2.10 2.43 3.05 2.70 2.23 1.98 1.60 1.30 1.20 1.15 1.07')})
diffuser_k_table=pd.concat([diffuser_k_table,Re6_row1_table,Re6_row2_table,Re6_row3_table,Re6_row4_table],ignore_index = True)
#---------------------------------------------------------------------------------------------------------------------------------
sudden_expansion_table = pd.DataFrame({'n_ar_inv':[],'Re':[],'Zeta':[]})

Re_list = [10,15,20,30,40,50,100,2e2,5e2,1e3,2e3,3e3,4e3]
row1 = pd.DataFrame({'n_ar_inv':[0.1]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 3.20 3.00 2.40 2.15 1.95 1.70 1.65 1.70 2.00 1.60 1.00 0.81')
                    })
row2 = pd.DataFrame({'n_ar_inv':[0.2]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 3.20 2.80 2.20 1.85 1.65 1.40 1.30 1.30 1.60 1.25 0.70 0.64')
                    })
row3 = pd.DataFrame({'n_ar_inv':[0.3]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 3.10 2.60 2.00 1.60 1.40 1.20 1.10 1.10 1.30 0.95 0.60 0.50')
                    })
row4 = pd.DataFrame({'n_ar_inv':[0.4]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 3.00 2.40 1.80 1.50 1.30 1.10 1.00 0.85 1.05 0.80 0.40 0.36')
                    })
row5 = pd.DataFrame({'n_ar_inv':[0.5]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 2.80 2.30 1.65 1.35 1.15 0.90 0.75 0.65 0.90 0.65 0.30 0.25')
                    })
row6 = pd.DataFrame({'n_ar_inv':[0.6]*len(Re_list),
                     'Re':Re_list,
                     'Zeta':f_toList('3.10 2.70 2.15 1.55 1.25 1.05 0.80 0.60 0.40 0.60 0.50 0.20 0.16')
                    })

sudden_expansion_table=pd.concat([sudden_expansion_table,row1,row2,row3,row4,row5,row6],ignore_index=True)

#********************************************************************************************************************************
st.subheader('Schematic and dimensions:')
link_extractor = 'https://github.com/VinPu/streamlit-example/blob/3543dcb99310bab05cac9e71b2d612b4d58886d9/extractor.png?raw=true'
st.image(link_extractor)

#Some constants @20 degC
density_air = 1.2 #kg/m^3
kinematic_vis_air = 1.5e-5 #m^2/s

#Target intake speed
Vel_F = 20 #m/s
Vel_F = st.number_input('Enter inlet air speed in m/s:')

st.subheader('Enter manifold dimensions in mm:')
#Design parameters all in meters
Dia_A = 200e-3
Dia_B = 200e-3
Dia_C = 150e-3
Dia_D = 35e-3
Dia_E = 32e-3
Dia_F = 32e-3

L1 = 100e-3
L2 = 80e-3
L3 = 50e-3
L4 = 30e-3
L5 = 80e-3

Dia_A = st.number_input('Diameter A') *1e-3
Dia_B = st.number_input('Diameter B') *1e-3
Dia_C = st.number_input('Diameter C') *1e-3
Dia_D = st.number_input('Diameter D') *1e-3
Dia_E = st.number_input('Diameter E') *1e-3
Dia_F = st.number_input('Diameter F') *1e-3

L1 = st.number_input('Section 1 length') *1e-3
L2 = st.number_input('Section 2 length') *1e-3
L3 = st.number_input('Section 3 length') *1e-3
L4 = st.number_input('Section 4 length') *1e-3
L5 = st.number_input('Section 5 length') *1e-3

#Surface roughness
delta = 0.15e-3 #Sheet steel

#Target volumetric flow rate
Q = Vel_F*4*3.14*(Dia_F/2)**2 #m^3/s



#*******************************************************************************************************************************
#Inlet pressure drop, assuming an optimal recirculation 'bellmouth' (Idelchik Page 153, Chapter 3, Paragraph 16; Diagram 3-4)
zeta_inlet = 0.12
P_dyn = density_air*Vel_F**2/2
dP_inlet = zeta_inlet * P_dyn

#Optimal bellmouth geometries
lip_length = Dia_F*0.25
lip_diameter = Dia_F*1.2

st.subheader('Inlet design:')
link_inlet = 'https://github.com/VinPu/streamlit-example/blob/36c943871390627d2dd83153bf3b02497a6533f0/Bellmouth.PNG?raw=true'
st.image(link_inlet)
nl = '\n'
st.text(f'Inlet pressure drop: {dP_inlet: .1f} Pa. Lip length: {1000*lip_length: .1f} mm. Lip diameter: {1000*lip_diameter: .1f} mm.')

#****************************************************************************************************************************************
st.subheader('Section 5: straight pipe after inlet.')
#Flow type
Re_5 = Vel_F*Dia_F/kinematic_vis_air

#Print results
st.text(f'Re = {Re_5: .1f}')
if Re_5>4000:
    st.text('Flow is turbulent.') 
    
#Starting length of turbulent flow
L_nonst_5 = Dia_F*(7.88*np.log10(Re_5) - 4.35)

#Print results
st.text(f'Starting length of turbulent flow = {1000*L_nonst_5: .1f} mm.')
if L_nonst_5 > L5:
    st.text(f'Longer than L5 ({1000*L5: .1f} mm), flow is non-stabilised.')

link_turb_start = 'https://github.com/VinPu/streamlit-example/blob/57a24c72ce96b9c8c8e15db7996fc1a55e28a9f9/TurbulentStart.PNG?raw=true'
st.image(link_turb_start)

link_turb_stable = 'https://github.com/VinPu/streamlit-example/blob/1849ca958aa0d183bc8fcf8092b88852cc895358/Turbulent_stabilised.PNG?raw=true'
st.image(link_turb_stable)

#Calculate straight stretch pressure loss
k_nonst_5 = 1.36*Re_5**0.05/(L5/Dia_F)**0.2
lambda_5 = 0.11*(delta/Dia_F + 68/Re_5)**0.25
zeta_5 = k_nonst_5*lambda_5*L5/Dia_F
P_dyn = density_air*Vel_F**2/2
dP_5 = zeta_5*P_dyn

#Print results
st.text(f'Section 5 pressure drop: {dP_5:.1f} Pa.')

#***************************************************************************************************************************************
st.subheader('Section 4: first diffuser after inlet.')
link_diffuser = 'https://github.com/VinPu/streamlit-example/blob/f69866801d00efc46ca43200ff4a5a478aeae7b8/Diffuser.PNG?raw=true'
st.image(link_diffuser)

#Diffuser parameters
n_ar_4 = (Dia_D/Dia_E)**2
Alpha_4 = 2 * np.arctan((Dia_D-Dia_E)/2 / L4) * 180/np.pi
LD_ratio_4 = L5/Dia_F

#Find best matching value of zeta_d
diffuser_zeta_table['Match'] = diffuser_zeta_table.apply(lambda row: abs(row.n_ar - n_ar_4)+
                                                                     abs(row.Re   - Re_5)+
                                                                     abs(row.Alpha - Alpha_4),axis=1)
idx_match = diffuser_zeta_table.idxmin().Match
zeta_d_4 = diffuser_zeta_table.iloc[idx_match,3]

#Find best matching value of k_d
diffuser_k_table['Match'] = diffuser_k_table.apply(lambda row: abs(row.n_ar - n_ar_4)+
                                                               abs(row.Re   - Re_5)+
                                                               abs(row.LD_ratio - LD_ratio_4)+
                                                               abs(row.Alpha - Alpha_4),axis=1)
idx_match = diffuser_k_table.idxmin().Match
k_d_4 = diffuser_k_table.iloc[idx_match,4]

#Print results
st.text(f'Zeta_d = {zeta_d_4:.3f}; k_d = {k_d_4:.3f}')

#Calculate diffuser pressure drop
P_dyn = density_air*Vel_F**2/2
dP_4 = k_d_4*zeta_d_4*P_dyn

#Print results
st.text(f'Section 4 pressure drop: {dP_4:.1f} Pa.')

#****************************************************************************************************************************************
st.subheader('Interface sec.4-sec.3: sudden expansion.')
#Expansion parameters
n_ar_inv_4t3 = 4*(Dia_D/2)**2 / (Dia_C/2)**2
Re_4 = (Q/(4*3.14*(Dia_D/2)**2)) * Dia_D / kinematic_vis_air

#Find best matching value of zeta
sudden_expansion_table['Match'] = sudden_expansion_table.apply(lambda row: abs(row.n_ar_inv - n_ar_inv_4t3)+
                                                                           abs(row.Re - Re_4), axis = 1)
idx_match = sudden_expansion_table.idxmin().Match
zeta_exp_4t3 = sudden_expansion_table.iloc[idx_match,2]

#Print results
st.text(f'Zeta_expansion = {zeta_exp_4t3:.2f}.')

#Calculate expansion pressure drop
P_dyn = density_air*(Q/(4*3.14*(Dia_D/2)**2))**2 / 2
dP_exp_4t3 = zeta_exp_4t3*P_dyn

st.text(f'Expansion pressure drop from section 4 to section 3: {dP_exp_4t3:.1f} Pa.')

#****************************************************************************************************************************************
st.subheader('Section 3: straight pipe.')
#Flow type
vel_3 = Q/(3.14*(Dia_C/2)**2)
Re_3 = vel_3 * Dia_C / kinematic_vis_air

#Starting length of turbulent flow
L_nonst_3 = Dia_C*(7.88*np.log10(Re_3) - 4.35)

#Calculate straight stretch pressure loss
k_nonst_3 = 1.36*Re_3**0.05/(L3/Dia_C)**0.2
lambda_3 = 0.11*(delta/Dia_C + 68/Re_3)**0.25
zeta_3 = k_nonst_3*lambda_3*L3/Dia_C
P_dyn = density_air*vel_3**2/2
dP_3 = zeta_3*P_dyn

#Print results
st.text(f'Section 3 pressure drop: {dP_3:.1f} Pa.')

#******************************************************************************************************************************************
st.subheader('Section 2: second diffuser.')
#Diffuser parameters
n_ar_2 = (Dia_B/Dia_C)**2
Alpha_2 = 2 * np.arctan((Dia_B-Dia_C)/2 / L2) * 180/np.pi
LD_ratio_2 = L3/Dia_C

#Find best matching value of zeta_d
diffuser_zeta_table['Match'] = diffuser_zeta_table.apply(lambda row: abs(row.n_ar - n_ar_2)+
                                                                     abs(row.Re   - Re_3)+
                                                                     abs(row.Alpha - Alpha_2),axis=1)
idx_match = diffuser_zeta_table.idxmin().Match
zeta_d_2 = diffuser_zeta_table.iloc[idx_match,3]

#Find best matching value of k_d
diffuser_k_table['Match'] = diffuser_k_table.apply(lambda row: abs(row.n_ar - n_ar_2)+
                                                               abs(row.Re   - Re_3)+
                                                               abs(row.LD_ratio - LD_ratio_2)+
                                                               abs(row.Alpha - Alpha_2),axis=1)
idx_match = diffuser_k_table.idxmin().Match
k_d_2 = diffuser_k_table.iloc[idx_match,4]

#Print results
st.text(f'Zeta_d = {zeta_d_2:.3f}; k_d = {k_d_2:.3f}')

#Calculate diffuser pressure drop
P_dyn = density_air*vel_3**2/2
dP_2 = k_d_2*zeta_d_2*P_dyn

#Print results
st.text(f'Section 2 pressure drop: {dP_2:.1f} Pa.')

#*******************************************************************************************************************************************
st.subheader('Section 1: straight pipe.')
#Flow type
vel_1 = Q/(3.14*(Dia_A/2)**2)
Re_1 = vel_1 * Dia_A / kinematic_vis_air

#Starting length of turbulent flow
L_nonst_1 = Dia_A*(7.88*np.log10(Re_1) - 4.35)

#Calculate straight stretch pressure loss
k_nonst_1 = 1.36*Re_1**0.05/(L1/Dia_A)**0.2
lambda_1 = 0.11*(delta/Dia_A + 68/Re_1)**0.25
zeta_1 = k_nonst_1*lambda_1*L1/Dia_A
P_dyn = density_air*vel_1**2/2
dP_1 = zeta_1*P_dyn

#Print results
st.text(f'Section 1 pressure drop: {dP_1:.1f} Pa.')

#***************************************************************************************************************************************
st.subheader('System specifications:')
P_total = dP_1 + dP_2 + dP_3 + dP_exp_4t3 + dP_4 + dP_5 + dP_inlet + density_air*vel_1**2/2
st.text(f'Air flow of {3600*Q:.1f} m3/hr.')
st.text(f'At pressure of {P_total:.1f} Pa.')
st.text(f'Estimated power is {Q*P_total/0.5:.1f} W.')






































