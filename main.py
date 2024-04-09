import argparse
from src.data_preprocessing.load_data import load_genomic_data
from src.data_preprocessing.clean_data import clean_genomic_data
from src.data_preprocessing.normalize_data import normalize_genomic_data
from src.models.train_model import train_disease_prediction_model
from src.models.predict import make_predictions

def main():
    parser = argparse.ArgumentParser(description="Genomic Disease Prediction Pipeline")
    
    parser.add_argument('--preprocess', action='store_true', help="Run data preprocessing steps")
    parser.add_argument('--train', action='store_true', help="Train the disease prediction model")
    parser.add_argument('--predict', action='store_true', help="Make predictions using the trained model")
    parser.add_argument('--data', type=str, help="Path to the input data file")
    parser.add_argument('--model', type=str, help="Path to the trained model file (for prediction)")
    
    args = parser.parse_args()

    if args.preprocess:
        print("Preprocessing genomic data...")
        data = load_genomic_data(args.data)
        data = clean_genomic_data(data)
        data = normalize_genomic_data(data)
        print("Data preprocessing completed.")

    if args.train:
        if not args.data:
            raise ValueError("Please provide the path to the preprocessed data for training.")
        print("Training disease prediction model...")
        train_disease_prediction_model(args.data)
        print("Model training completed.")

    if args.predict:
        if not args.data or not args.model:
            raise ValueError("Please provide the path to the data and the trained model for making predictions.")
        print("Making predictions...")
        predictions = make_predictions(args.data, args.model)
        print("Predictions completed:")
        print(predictions)

if __name__ == '__main__':
    main()
