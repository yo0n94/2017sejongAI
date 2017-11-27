import numpy as np
from sklearn import preprocessing


#샘플 데이터 정의
input_data = np.array([[3.7, -1.8, 4.8],
                      [-1.0, 5.6, -4.2],
                      [3.9, 0.9, 1.6],
                      [6.2, -8.9, -5.4]])

#데이터 이진화
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("\nBinarized data : \n", data_binarized)

#평균과 표준편차 출력
print("\n BEFORE : ")
print("Mean = ", input_data.mean(axis=0))
print("Std deviation = ", input_data.std(axis=0))

#평균 제거
data_scaed = preprocessing.scale(input_data)
print("\n AFTER : ")
print("Mean = ", data_scaed.mean(axis=0))
print("Std deviation = ", data_scaed.std(axis=0))


#크기 조정
#최솟값 /최댓값 조정
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data : \n", data_scaled_minmax)

#정규화
#데이터 정규화
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 normalized data : \n", data_normalized_l1)
print("\nL1 normalized data : \n", data_normalized_l2)