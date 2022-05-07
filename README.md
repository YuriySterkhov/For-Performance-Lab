Домашнее задание по курсу "Linux основы"


Задание 1

Ответ: дистрибутивы DEB: Debian, Ubuntu; дистрибутивы RPM: Red Hat, Fedora.

Задание 2

Ответ: команда, возможно, должна была передать количество строк, куда входит слово root в конец файла, но расширение файла не указано, и команда не сработает.

Задание 3

Ответ: ps -aux | grep root  >> user_root_ps.txt

Задание 4

Ответ: команда vmstat позволяет вывести информацию об использовании памяти, дисков, процессора. 
si (swap in) – количество блоков в секунду, которое система считывает из раздела или файла swap в память;
so (swap out) – и наоборот, количество блоков в секунду, которое система перемещает из памяти в swap.

Задание 5

Ответ: 

lscpu
cat cpuinfo
cat meminfo|grep Inactive

Задание 6

Ответ:
 

Создайте скрин вывода команды free -h -t
Создайте swap-файл размером 512 Мб в корне диска / с именем swapfile
Добавьте настройку чтобы swap-файл подключался автоматически при перезагрузке виртуальной машины (подсказка: необходимо внести изменения в файл /etc/fstab)
Создайте скрин вывода команды free -h -t
Создайте скрин вывода команды swapon -s
В качестве ответа приложите созданные скриншоты

Задание 7

Ответ:

Задание 8

Ответ: влияет, так как load average показывает среднюю нагрузку операционной системы по процессору, памяти и  количеству операций ввода-вывода жесткого диска.

Задание 9

Ответ:   hardlink  указывает на inode, содержимое файла, а softlink - указывает на имя файла, а не на его содержимое.

Задание 10

Ответ: команда df -i выводит на экран таблицу: 1 графа - общее количество inodes, 2 графа - количество свободных inodes, 3 графа - количество используемых inodes, 4 графа - процент используемых inodes.

Задание 11

Ответ: События, при которых выполнение процесса переходит в режим ядра — аппаратные прерывания, особые ситуации и системные вызовы. Во всех случаях ядро получает управление и вызывает соответствующую системную процедуру для обработки события. Перед вызовом ядро сохраняет состояние прерванного процесса в системном стеке. После завершения обработки, состояние процесса восстанавливается и процесс возвращается в исходный режим выполнения. Чаще всего это режим задачи, но если, например, прерывание возникло, когда процесс уже находился в режиме ядра, после обработки события он останется в этом режиме.

Задание 12

Ответ: 
![image](https://user-images.githubusercontent.com/101258126/167260583-cb5c5fa0-22e3-4c3d-840b-7516ca251047.png)
 

Задание 13

Ответ:

Задание 14

Ответ:
