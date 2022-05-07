Домашнее задание по курсу "Linux основы"


Задание 1

Ответ: дистрибутивы DEB: Debian, Ubuntu; дистрибутивы RPM: Red Hat, Fedora.

Задание 2

Объясните, что делает команда:
ps -aux | grep root | wc -l >> root
Ответ напишите в свободной форме

Задание 3

Напишите команду, которая вывод все запущенные процессы пользователя root в файл "user_root_ps"

Задание 4
Ответ: команда vmstat позволяет вывести информацию об использовании памяти, дисков, процессора. 
si (swap in) – количество блоков в секунду, которое система считывает из раздела или файла swap в память;
so (swap out) – и наоборот, количество блоков в секунду, которое система перемещает из памяти в swap.

Задание 5

Приведите 3 команды, которые выведут на экран следующее:

Архитектуру ПК
Модель процессора
Количество памяти, которая уже не используется процессами, но еще остается в памяти(ключевое слово - inactive).
Примечание: при выполнении задания предполагается использование конструкции "{команда} | grep {параметр для фильтрации вывода}" в каталоге /proc

Задание 6

Создайте скрин вывода команды free -h -t
Создайте swap-файл размером 512 Мб в корне диска / с именем swapfile
Добавьте настройку чтобы swap-файл подключался автоматически при перезагрузке виртуальной машины (подсказка: необходимо внести изменения в файл /etc/fstab)
Создайте скрин вывода команды free -h -t
Создайте скрин вывода команды swapon -s
В качестве ответа приложите созданные скриншоты

Задание 7

Найдите информацию про tmpfs.
Расскажите в свободной форме, в каких случаях уместно использовать эту технологию.
Создайте диск tmpfs (размер не более 512Мб), смонтируйте его в директорию /mytmpfs
В качестве ответа приведите скриншот вывода команды df- h до и после монтирования диска tmpfs.

Задание 8

Влияет ли количество операций ввода-вывода HDD диска на параметр load average?
Приведите развернутый ответ в свободной форме

Задание 9

Чем hardlink отличается от softlink?
Приведите ответ в свободной форме

Задание 10
Ответ: команда df -i выводит на экран таблицу: 1 графа - общее количество inodes, 2 графа - количество свободных inodes, 3 графа - количество используемых inodes, 4 графа - процент используемых inodes.

Задание 11
Ответ: События, при которых выполнение процесса переходит в режим ядра — аппаратные прерывания, особые ситуации и системные вызовы. Во всех случаях ядро получает управление и вызывает соответствующую системную процедуру для обработки события. Перед вызовом ядро сохраняет состояние прерванного процесса в системном стеке. После завершения обработки, состояние процесса восстанавливается и процесс возвращается в исходный режим выполнения. Чаще всего это режим задачи, но если, например, прерывание возникло, когда процесс уже находился в режиме ядра, после обработки события он останется в этом режиме.

Задание 12

Найдите имя автора модуля libcrc32c при помощи утилиты modinfo
В качестве ответа приложите скриншот вывода команды

Задание 13

Используя утилиту strace выясните какой системный вызов использует команда cd
Примечание: она не является внешним файлом, но для наших целей использовать: strace -c bash 'cd /tmp'
В качестве ответа напишите название системного вызова или нескольких вызовов

Задание 14

Существует такой вид виртуализации как контейнеризация: контейнеры создаются на уровне ОС и работают в изолированных пространствах.
Вопрос: что произойдет, если в хостовой ОС установлен upstart или systemV, а в запущенном контейнере - systemd?
Приведите ответ в свободной форме со своим комментарием.
