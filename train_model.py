from utils.config_loader import load_config_model
from utils.plot_metrics import plot_metrics
from utils.save_model import save_model
from loader_dataset.loader_dataset import LoaderDataset
from model.model_mnist import ModelMNIST
from trainer.trainer import Trainer


model = ModelMNIST()
criterion, optimizer, epochs = load_config_model(model)

loader_train_set = LoaderDataset.get_mnist_loader_dataset(True, 2000, 10000)
loader_eval_set  = LoaderDataset.get_mnist_loader_dataset(False, 500, 2500)

training_losses, training_accuracies, evaluation_losses, evaluation_accuracies = \
    Trainer.train_eval(model, criterion, optimizer, loader_train_set, loader_eval_set, epochs)

plot_metrics(training_losses, training_accuracies, evaluation_losses, evaluation_accuracies)

save_model(model)
