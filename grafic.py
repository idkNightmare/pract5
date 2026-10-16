import matplotlib.pyplot as plt 
import numpy as np

rng = np.random.default_rng()
grate = rng.integers(0, 101, size=(100, 3))

math_grades = grate[:, 0]
english_grades = grate[:, 1]
prog_grades = grate[:, 2]
math_groups = grate[:, 0].reshape(10, 10).mean(axis=1)
english_groups = grate[:, 1].reshape(10, 10).mean(axis=1)
prog_groups = grate[:, 2].reshape(10, 10).mean(axis=1)
group_numbers = np.arange(1, 11)
colors_bar=['#0000FF','#FFFF00','#FF0000','#1D3557','#4EA8DE']
colors_hist=['skyblue','red','green']
all_predmets=['Математика','Англійська','Програмування']
predmet=['Математика','Інші предмети','Англійська','Програмування']
spend_time_student=[30,10,20,40]
students_ids = np.arange(1, 101)
width = 0.25

plt.figure(figsize=(14, 6),layout='constrained')

plt.subplot(221)
plt.plot(students_ids, prog_grades, marker='o', markersize=4, linestyle='-', color='royalblue', label='Оцінка з Програмування')
plt.title('Графік оцінок з програмування для всіх студентів', fontsize=14, fontweight='bold')
plt.xlabel('ID Студента', fontsize=12)
plt.ylabel('Бали (0 - 100)', fontsize=12)
plt.xticks(np.arange(0, 101, 5))
plt.ylim(-5, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')

plt.subplot(222)
plt.bar(students_ids[:10],math_grades[:10],color=colors_bar,edgecolor='black')
plt.title("Оцінки студентів з математики")
plt.ylabel("Бал")
plt.xticks(students_ids[:10])
plt.ylim(0,105)

plt.subplot(223)
plt.pie(spend_time_student,labels=predmet,autopct='%1.1f%%')
plt.title('Витрачений час студентів на предмети')

plt.subplot(224)
plt.bar(group_numbers - width, math_groups, width=width, color=colors_hist[0], edgecolor='red', label=all_predmets[0])
plt.bar(group_numbers, english_groups, width=width, color=colors_hist[1], edgecolor='red', label=all_predmets[1])
plt.bar(group_numbers + width, prog_groups, width=width, color=colors_hist[2], edgecolor='red', label=all_predmets[2])
plt.title('Середній бал по групах (з 10 студентів)')
plt.xlabel('Номер групи')
plt.ylabel('Середній бал')
plt.xticks(group_numbers)
plt.ylim(0, 105)

plt.legend(loc='upper right')
plt.tight_layout()

plt.subplots_adjust(hspace=0.3,wspace=0.3)
plt.savefig('grafics.png')  
plt.show()