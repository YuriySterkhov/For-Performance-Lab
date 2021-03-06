Домашнее задание по курсу "Linux основы"


Задание 1

Ответ: дистрибутивы DEB: Debian, Ubuntu; дистрибутивы RPM: Red Hat, Fedora.

Задание 2

Ответ: наличие в команде символов | и >> говорит о перенаправлении стандартного потока вывода данных, ps –aux выводит на экран все запущенные процессы пользователя, но использование | перенаправляет вывод на вход команды grep root. grep root находит процессы со словом root в запущенных процессах пользователя, но не выводит на экран строки, так как | снова перенаправляет вывод, теперь команде ws –l. ws –l считает количество строк, полученных на вход, но снова не выводит на экран, так как >> перенаправляет вывод в файл root так, что данные будут дописаны в конец файла root. Такое последовательное сочетание команд и перенаправлений стандартного потока вывода в результате выполнения даёт запись в конце файла root – количество всех запущенных процессов пользователя root в виде целого значения.

Задание 3

Ответ: ps -aux | grep root >> user_root_ps без потери данных в исходном файле, так как данные будут записаны в конец файла; ps -aux | grep root > user_root_ps с потерей данных в исходном файле, так как он будет перезаписан.

Задание 4

Ответ: команда vmstat позволяет вывести информацию об использовании памяти, дисков, процессора. 
si (swap in) – количество блоков в секунду, которое система считывает из раздела или файла swap в память;
so (swap out) – и наоборот, количество блоков в секунду, которое система перемещает из памяти в swap.

Задание 5

Ответ: 

arch

cat /proc/cpuinfo | grep 'model name'

cat /proc/meminfo | grep 'Inact'


Задание 6

Ответ:

![image](https://user-images.githubusercontent.com/101258126/169710098-0b56a767-b820-46dc-9b35-fd5f68351d56.png)

![image](https://user-images.githubusercontent.com/101258126/169710103-ce3753c9-317d-49b1-a55d-ee71c29eb97d.png)

![image](https://user-images.githubusercontent.com/101258126/169710109-b812f4d3-a1f8-4e50-b492-c41f77df3a41.png)


Задание 7

Ответ: tmpfs — временное файловое хранилище во многих Unix-подобных ОС. Предназначена для монтирования файловой системы, но размещается в ОЗУ вместо физического диска. В tmpfs могут быть размещены любые каталоги, хранящие временные данные, удаляемые при перезагрузке системы: /var/lock, /var/run, /tmp и др. Кроме того, для уменьшения количества дисковых операций (в целях максимального повышения производительности системы или экономии ресурса твердотельных накопителей) в tmpfs иногда размещают каталоги, которые обычно хранят данные между перезагрузками или каталоги кэширования некоторых программ. Следует помнить, что все данные, размещённые в tmpfs, после перезагрузки будут утрачены.

![image](https://user-images.githubusercontent.com/101258126/169710278-5b068128-e51f-402f-b578-45aa795df1fe.png)

![image](https://user-images.githubusercontent.com/101258126/169710283-726d7c1d-e7e5-4b2a-921e-7ef2a2e18f88.png)

Задание 8

Ответ: влияет, так как load average показывает среднюю нагрузку операционной системы по процессору, памяти и  количеству операций ввода-вывода жесткого диска.

Задание 9

Ответ:

Особенности hardlink:
- работают только в пределах одной файловой системы;
- нельзя ссылаться на каталоги;
- имеют ту же информацию inode и набор разрешений, что и у исходного файла;
- разрешения на ссылку изменяются при изменении разрешений файла;
- можно перемещать и переименовывать и даже удалять файл без вреда ссылке.

Особенности softlink:
- можно ссылаться на другие разделы диска;
- можно ссылаться на файлы и каталоги;
- содержат только имя файла, а не его содержимое, а права доступа и номер inode отличаются от исходного файла;
- при изменении прав доступа для исходного файла, права на ссылку останутся неизменными;
- после удаления, перемещения или переименования файла ссылки становятся недействительными.

Задание 10

Ответ: команда df -i выводит на экран таблицу: 1 графа - общее количество inodes, 2 графа - количество свободных inodes, 3 графа - количество используемых inodes, 4 графа - процент используемых inodes.

Задание 11

Ответ: События, при которых выполнение процесса переходит в режим ядра — аппаратные прерывания, особые ситуации и системные вызовы. Во всех случаях ядро получает управление и вызывает соответствующую системную процедуру для обработки события. Перед вызовом ядро сохраняет состояние прерванного процесса в системном стеке. После завершения обработки состояние процесса восстанавливается, и процесс возвращается в исходный режим выполнения. Чаще всего это режим задачи, но если, например, прерывание возникло, когда процесс уже находился в режиме ядра, после обработки события он останется в этом режиме.

Задание 12

Ответ:

![image](https://user-images.githubusercontent.com/101258126/167260738-00139ff1-ae07-4088-a401-ca84a14c83ce.png)


Задание 13

Ответ: read, write, close и др.

Задание 14

Ответ: если учесть, что контейнеризация это метод виртуализации, при котором ядро операционной системы поддерживает несколько изолированных экземпляров пространства пользователя вместо одного, причём эти экземпляры с точки зрения выполняемых в них процессов идентичны отдельному экземпляру операционной системы; то, видимо, хостовая ОС и контейнер должны работать, «не замечая» друг друга. А появление какого-то сбоя станет свидетельством несовершенства технологии контейнеризации.
