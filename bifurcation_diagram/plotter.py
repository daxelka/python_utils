import matplotlib.pyplot as plt

class BifurcationDiagramPlotter:

    def plot(self, x, y, x_label = 'bifurcation parameter', y_label= 'y variable'):
        plt.rcParams['font.size'] = '12'
        plt.scatter(x, y, marker='.', color='black', s=1)
        plt.xlabel(x_label,fontsize=14)
        plt.ylabel(y_label,fontsize=14)
        plt.savefig('/Users/daxelka/Library/Mobile Documents/com~apple~CloudDocs/Documents/Modeling/Deffuant_model/ba_formation/Deffuant/result2.png')
        plt.show()


