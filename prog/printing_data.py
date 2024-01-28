from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

colors = list(mcolors.TABLEAU_COLORS.values())

def files(lines, data, genre):
    for line in lines:
        name, x, time_str = line.strip().split(':')

        if name not in data:
            data[name] = {'times': [], genre: []}

        data[name]['times'].append(time_str) 
        data[name][f'{genre}'].append(float(x))

def plot_line_and_text(data, genre, line_values, color, label, ax):
    for name, values in data.items():
      
        line = line_values(values[genre])
        ax.plot(values['times'], line, linestyle='--', color=color,linewidth=3, label=f'{label} {genre}')


def plot_individual(data, fname, direc, genre):
        
    
    for name, values in data.items():
        
        plt.figure(figsize=(45, 20)) 
        plt.plot(values['times'], values[genre], marker="o", linestyle='-', label=name,
                 color=colors[len(plt.gca().lines) % len(colors)], linewidth=4, markersize=8, markerfacecolor='red')

        plt.yticks(fontsize=20)
        plt.xlabel('Temps', fontsize=20, fontweight='bold')
        plt.ylabel(f'{genre}(%)', fontsize=20)
        plt.title(f'{genre} - {name}', fontsize=24)
        plt.grid(True)

        avg_values =  round(sum(values[genre]) / len(values[genre]), 2)
        min_values = min(values[genre])
        max_values = max(values[genre])
        ecart_type_values = ecart_type(values[genre])

        plot_line_and_text({name: values}, genre, lambda x: [sum(x) / len(x)] * len(x), 'red', 'Moyenne', plt.gca())
        plot_line_and_text({name: values}, genre, lambda x: [min(x)] * len(x), 'green', 'Minimum', plt.gca())
        plot_line_and_text({name: values}, genre, lambda x: [max(x)] * len(x), 'orange', 'Maximum', plt.gca())
        
        plt.text(0.965, 0.55, f'moyenne {genre}: {avg_values:.2f}%', transform=plt.gca().transAxes, fontsize=17, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        plt.text(0.965, 0.50, f'Minimum {genre}: {min_values:.2f}%', transform=plt.gca().transAxes, fontsize=17, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        plt.text(0.965, 0.45, f'Maximum {genre}: {max_values:.2f}%', transform=plt.gca().transAxes, fontsize=17, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        plt.text(0.965, 0.4, f'Ecart Type {genre}: {ecart_type_values:.2f}', transform=plt.gca().transAxes, fontsize=17, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))


        # Access the legend object and set font size
        legend = plt.gca().legend(bbox_to_anchor=(0.96,0.96))
        if legend:
            for text in legend.get_texts():
                text.set_fontsize(18)
                text.set_fontweight('bold')

        save_filename = os.path.join(f'./charts/{genre}/{direc}', f'{fname}-{name}.png')
        plt.savefig(save_filename)
        plt.close()

def plot_total(data, fname, direc, genre):
    plt.figure(figsize=(45, 20))  
    for name, values in data.items():
        plt.plot(values['times'], values[genre], linestyle='-', label=name,
                 color=colors[len(plt.gca().lines) % len(colors)], linewidth=1.5)

    plt.xlabel('Temps', fontsize=20, fontweight='bold')
    plt.ylabel(f'{genre}(%)', fontsize=20)
    plt.title(f'{genre} - Total', fontsize=24)

    plt.grid(True)

    plt.legend(loc='upper left', bbox_to_anchor=(0.96, 1), fontsize=14)

    save_filename = os.path.join(f'./charts/{genre}/{direc}', f'{fname}-total.png')
    plt.savefig(save_filename)
    plt.close()


def ecart_type(values):
    l = values.copy()
    moy = round(sum(l) / len(l), 2)

    for x in range(len(l)):
        l[x] -= moy
        l[x] = pow(l[x], 2)

    variance = sum(l) / (len(l) - 1)
    ecart = round(sqrt(variance), 2)
    return ecart

fname = [('occup-bikes', 'bikes', 'occupations', 'utf-8'),
         ('occup-cars', 'cars', 'occupations', 'utf-8'),
         ('avg_bikes', 'bikes', 'moyenne_remplissage', 'ISO-8859-1'),
         ('avg_cars', 'cars', 'moyenne_remplissage', 'ISO-8859-1')]

for i in fname:
    with open(f'{i[0]}.txt', encoding=i[3]) as file:
        data = {}
        print(i[0])
        lines = file.readlines()
        files(lines, data, i[2])
        plot_individual(data, i[0], i[1], i[2])
        plot_total(data, i[0], i[1], i[2])
