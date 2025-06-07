import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def load_and_prepare_data(file_path):
    original_data = pd.read_csv(file_path)
    data = original_data.copy()

    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        if data[col].isnull().any():
            data[col] = data[col].fillna(data[col].median())

    scaler = MinMaxScaler()
    features = ['bill_length_mm', 'bill_depth_mm']
    data[features] = scaler.fit_transform(data[features])

    return data, scaler, original_data

def apply_kmeans(data, features, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    data['cluster'] = model.fit_predict(data[features])
    return model

def evaluate_kmeans_accuracy(data, cluster_to_species):
    predicted_labels = data['cluster'].map(cluster_to_species)
    accuracy = (predicted_labels == data['species']).mean() * 100
    print(f"K-Means Model Doğruluğu: {float(accuracy):.2f}%")

def evaluate_knn_accuracy(model, data, features):
    predictions = model.predict(data[features])
    accuracy = accuracy_score(data['species'], predictions) * 100
    print(f"KNN Modeli Doğruluğu: {accuracy:.2f}%")

def predict_new_data(new_point_scaled, data, features, kmeans_model, cluster_to_species, knn_model):
    new_df = pd.DataFrame([new_point_scaled], columns=features)
    cluster = kmeans_model.predict(new_df)[0]
    kmeans_species = cluster_to_species.get(cluster, "Bilinmeyen")
    knn_species = knn_model.predict(new_df)[0]

    print(f"K-Means tahmini: {kmeans_species}")
    print(f"KNN tahmini: {knn_species}")
    if kmeans_species == knn_species:
        print("Tahminler uyuştu.")
    else:
        print("Tahminler uyuşmuyor.")

def plot_kmeans_predictions(data, kmeans_model, features, cluster_to_species, new_point=None):
    colors = {'Adelie': 'green', 'Chinstrap': 'red', 'Gentoo': 'black'}
    data['kmeans_pred'] = data['cluster'].map(cluster_to_species)

    plt.figure(figsize=(8, 6))
    for species in data['kmeans_pred'].unique():
        subset = data[data['kmeans_pred'] == species]
        plt.scatter(subset[features[0]], subset[features[1]], color=colors[species], label=species)

    plt.scatter(*kmeans_model.cluster_centers_.T, color='purple', marker='*', s=200, label='K-Means Merkez')
    if new_point:
        plt.scatter(*new_point, color='blue', label='Yeni Veri', s=100, edgecolor='white')

    plt.title('K-Means Kümeleme Tahminleri')
    plt.xlabel('Gaga Uzunluğu (ölçeklenmiş)')
    plt.ylabel('Gaga Yüksekliği (ölçeklenmiş)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_knn_predictions(data, features, model, new_point=None):
    colors = {'Adelie': 'green', 'Chinstrap': 'red', 'Gentoo': 'black'}
    data['knn_pred'] = model.predict(data[features])

    plt.figure(figsize=(8, 6))
    for species in data['knn_pred'].unique():
        subset = data[data['knn_pred'] == species]
        plt.scatter(subset[features[0]], subset[features[1]], color=colors[species], label=species)

    if new_point:
        plt.scatter(*new_point, color='blue', label='Yeni Veri', s=100, edgecolor='white')

    plt.title('KNN Sınıflandırma Tahminleri')
    plt.xlabel('Gaga Uzunluğu (ölçeklenmiş)')
    plt.ylabel('Gaga Yüksekliği (ölçeklenmiş)')
    plt.legend()
    plt.grid(True)
    plt.show()

def show_confusion_between_kmeans_knn(data):
    cm = confusion_matrix(data['kmeans_pred'], data['knn_pred'], labels=data['species'].unique())
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data['species'].unique())
    disp.plot(cmap='Blues')
    plt.title("K-Means vs KNN Confusion Matrix")
    plt.grid(False)
    plt.show()

def calculate_kmeans_knn_agreement(data):
    if 'kmeans_pred' not in data.columns or 'knn_pred' not in data.columns:
        print("Lütfen önce tahminleri hesaplayın.")
        return
    total = len(data)
    match_count = (data['kmeans_pred'] == data['knn_pred']).sum()
    agreement_rate = (match_count / total) * 100
    print(f"K-Means ve KNN tahminlerinin uyum oranı: {agreement_rate:.2f}%")

def main():
    file_path = "data/penguins.csv"
    features = ['bill_length_mm', 'bill_depth_mm']

    data, scaler, original_data = load_and_prepare_data(file_path)
    kmeans_model = apply_kmeans(data, features)
    cluster_to_species = data.groupby('cluster')['species'].agg(lambda x: x.mode()[0]).to_dict()

    k = int(input("K değeri (1-10 arası): "))
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(data[features], data['species'])

    evaluate_knn_accuracy(knn_model, data, features)
    evaluate_kmeans_accuracy(data, cluster_to_species)

    min_len = original_data['bill_length_mm'].min()
    max_len = original_data['bill_length_mm'].max()
    min_depth = original_data['bill_depth_mm'].min()
    max_depth = original_data['bill_depth_mm'].max()

    l = float(input(f"Gaga uzunluğu ({min_len:.1f}-{max_len:.1f} mm): "))
    d = float(input(f"Gaga yüksekliği ({min_depth:.1f}-{max_depth:.1f} mm): "))

    new_data_df = pd.DataFrame([[l, d]], columns=features)
    l_scaled, d_scaled = scaler.transform(new_data_df)[0]
    new_point = (l_scaled, d_scaled)

    plot_kmeans_predictions(data, kmeans_model, features, cluster_to_species, new_point)
    plot_knn_predictions(data, features, knn_model, new_point)

    predict_new_data(new_point, data, features, kmeans_model, cluster_to_species, knn_model)
    show_confusion_between_kmeans_knn(data)
    calculate_kmeans_knn_agreement(data)

if __name__ == "__main__":
    main()

  
