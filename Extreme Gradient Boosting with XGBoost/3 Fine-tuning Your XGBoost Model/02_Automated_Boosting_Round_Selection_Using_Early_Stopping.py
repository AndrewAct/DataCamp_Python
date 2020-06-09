# # 6/7/2020
# Now, instead of attempting to cherry pick the best possible number of boosting rounds, you can very easily have XGBoost automatically select the number of boosting rounds for you within xgb.cv(). This is done using a technique called early stopping.

# Early stopping works by testing the XGBoost model after every boosting round against a hold-out dataset and stopping the creation of additional boosting rounds (thereby finishing training of the model early) if the hold-out metric ("rmse" in our case) does not improve for a given number of rounds. Here you will use the early_stopping_rounds parameter in xgb.cv() with a large possible number of boosting rounds (50). Bear in mind that if the holdout metric continuously improves up through when num_boost_rounds is reached, then early stopping does not occur.

# Here, the DMatrix and parameter dictionary have been created for you. Your task is to use cross-validation with early stopping. Go for it!

# Create your housing DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary for each tree: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation with early stopping: cv_results
cv_results = xgb.cv(dtrain= housing_dmatrix, params= params, nfold = 3, early_stopping_rounds= 10,
                    num_boost_round = 50, metrics= "rmse", as_pandas = True, seed = 123)

# Print cv_results
print(cv_results)

# script.py> output:
#     [03:48:49] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:48:50] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:48:50] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#         train-rmse-mean  train-rmse-std  test-rmse-mean  test-rmse-std
#     0     141871.630208      403.632626   142640.656250     705.559400
#     1     103057.036458       73.769561   104907.661458     111.116005
#     2      75975.968750      253.729626    79262.057291     563.767892
#     3      57420.531250      521.656754    61620.135417    1087.692943
#     4      44552.955729      544.170190    50437.561198    1846.446330
#     5      35763.946615      681.797429    43035.661458    2034.469207
#     6      29861.464844      769.572907    38600.880208    2169.796232
#     7      25994.675781      756.521419    36071.817708    2109.795430
#     8      23306.836588      759.238254    34383.184896    1934.546688
#     9      21459.769531      745.624998    33509.141276    1887.375284
#     10     20148.720703      749.612103    32916.808594    1850.894249
#     11     19215.382812      641.388842    32197.833984    1734.456073
#     12     18627.388672      716.256238    31770.852865    1802.155484
#     13     17960.694661      557.043073    31482.781250    1779.124592
#     14     17559.736979      631.412969    31389.991537    1892.319150
#     15     17205.712565      590.171852    31302.881511    1955.165830
#     16     16876.571940      703.631755    31234.058594    1880.705796
#     17     16597.662435      703.677150    31318.348959    1828.860617
#     18     16330.460937      607.274494    31323.633464    1775.909418
#     19     16005.972982      520.470911    31204.135417    1739.076156
#     20     15814.301107      518.604934    31089.862630    1756.021674
#     21     15493.405924      505.616658    31047.996094    1624.673955
#     22     15270.734700      502.018618    31056.916015    1668.042812
#     23     15086.382162      503.913199    31024.983724    1548.985354
#     24     14917.608724      486.206468    30983.684896    1663.128987
#     25     14709.589518      449.668010    30989.477214    1686.666560
#     26     14457.286133      376.787666    30952.114583    1613.172955
#     27     14185.567383      383.102234    31066.901693    1648.534014
#     28     13934.067057      473.464991    31095.641276    1709.225654
#     29     13749.645182      473.670437    31103.886068    1778.879154
#     30     13549.836589      454.898834    30976.085286    1744.515995
#     31     13413.485351      399.603618    30938.470052    1746.052979
#     32     13275.916016      415.408786    30931.000651    1772.469906
#     33     13085.878255      493.792509    30929.056640    1765.540153
#     34     12947.181315      517.790039    30890.630208    1786.511479
#     35     12846.026693      547.732724    30884.492839    1769.728719
#     36     12702.378581      505.523315    30833.542969    1691.003483
#     37     12532.244141      508.298241    30856.688151    1771.446377
#     38     12384.054687      536.224681    30818.016927    1782.784630
#     39     12198.444336      545.165562    30839.393229    1847.327435
#     40     12054.583333      508.841412    30776.966146    1912.780507
#     41     11897.036784      477.177937    30794.701823    1919.674347
#     42     11756.221680      502.992782    30780.956380    1906.819587
#     43     11618.846354      519.837088    30783.755208    1951.258863
#     44     11484.080404      578.427828    30776.731120    1953.446309
#     45     11356.553060      565.368380    30758.543620    1947.454953
#     46     11193.558594      552.298906    30729.971354    1985.700237
#     47     11071.315429      604.089960    30732.663411    1966.997809
#     48     10950.778320      574.862779    30712.241536    1957.750197
#     49     10824.865885      576.665756    30720.854818    1950.511520

# <script.py> output:
#     [03:49:18] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:49:18] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:49:19] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#         train-rmse-mean  train-rmse-std  test-rmse-mean  test-rmse-std
#     0     141871.635417      403.636200   142640.656250     705.559400
#     1     103057.036458       73.769561   104907.664062     111.112417
#     2      75975.966146      253.726099    79262.059895     563.766991
#     3      57420.531250      521.656754    61620.136719    1087.694282
#     4      44552.954427      544.171560    50437.562500    1846.448017
#     5      35763.946615      681.797429    43035.661458    2034.469207
#     6      29861.464193      769.571238    38600.880208    2169.796232
#     7      25994.675130      756.519115    36071.817708    2109.795430
#     8      23306.836588      759.238254    34383.184896    1934.546688
#     9      21459.769531      745.626217    33509.141276    1887.375284
#     10     20148.721354      749.612769    32916.807943    1850.894475
#     11     19215.382812      641.388842    32197.833984    1734.456073
#     12     18627.388672      716.256238    31770.853516    1802.155409
#     13     17960.694661      557.043073    31482.781901    1779.124534
#     14     17559.736328      631.412555    31389.990886    1892.319967
#     15     17205.712891      590.171393    31302.882162    1955.165902
#     16     16876.571940      703.631755    31234.058594    1880.705796
#     17     16597.662110      703.677609    31318.348959    1828.860617
#     18     16330.460937      607.274494    31323.632813    1775.909171
#     19     16005.973307      520.471073    31204.134766    1739.077059
#     20     15814.301107      518.604304    31089.862630    1756.021674
#     21     15493.406250      505.616236    31047.995443    1624.674840
#     22     15270.734375      502.018328    31056.916015    1668.042812
#     23     15086.382162      503.913199    31024.984375    1548.985605
#     24     14917.608724      486.206468    30983.684896    1663.130201
#     25     14709.589844      449.668224    30989.476563    1686.667469
#     26     14457.286133      376.787666    30952.113281    1613.173549
#     27     14185.567383      383.102234    31066.901693    1648.533703
#     28     13934.067057      473.465714    31095.641276    1709.225654
#     29     13749.645182      473.670437    31103.887370    1778.880069
#     30     13549.836589      454.898052    30976.085287    1744.514533
#     31     13413.485351      399.603618    30938.468750    1746.052063
#     32     13275.915690      415.408663    30931.000000    1772.469510
#     33     13085.878581      493.792860    30929.056640    1765.540153
#     34     12947.181641      517.790106    30890.630208    1786.511392
#     35     12846.027018      547.732291    30884.493490    1769.729215
#     36     12702.378906      505.522878    30833.541667    1691.002487
#     37     12532.244466      508.298594    30856.688151    1771.445059
#     38     12384.055013      536.225042    30818.017578    1782.785133
#     39     12198.444010      545.165197    30839.393880    1847.326516
#     40     12054.583333      508.841412    30776.966146    1912.780507
#     41     11897.036458      477.177568    30794.702474    1919.674832
#     42     11756.221354      502.992395    30780.955729    1906.819146
#     43     11618.846680      519.837120    30783.756511    1951.259784
#     44     11484.080078      578.428250    30776.731120    1953.446309
#     45     11356.553060      565.368380    30758.543620    1947.454953
#     46     11193.558268      552.298848    30729.972005    1985.699316
#     47     11071.315429      604.089960    30732.663411    1966.997822
#     48     10950.777995      574.863209    30712.242187    1957.750652
#     49     10824.865560      576.665405    30720.854818    1950.511520