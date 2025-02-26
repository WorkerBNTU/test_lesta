# test_lesta
## Test 1
Проверка на четность.
### 1 функция:
В данной функции используется побитовая операция И - `&`. Без объяснений о том, что все целые числа могут быть представлены в двоичном виде, сразу переходим к побитовому И. Кратко: это сравнение количества "единиц" в указанных числах.
Более подробно: так как число 1 в любой разрядности имеет единицу в последнем разряде и нули в остальных, нас интересует только последний разряд исходного числа. В результате мы получаем 1 (если последний разряд числа в двоичном представлении равен 1, что означает совпадение 1 разряда с 1) или 0 (если последний разряд - 0). Любое нечетное число в двоичной системе заканчивается на 1.

**Плюсы и минусы вашей реализации:** адекватность, но менее эффективность (под капотом).  
**Плюсы и минусы моей:** противоположные.

### 2 функция:
Не требует пояснений.

**Плюсы и минусы по сравнению с исходной:** ещё менее адекватная, но временная сложность больше; из плюсов - только веселье.

## Test 2
Для начала рассмотрим, как я понял принцип FIFO и такой структуры данных.
Поскольку в задании написано **"циклический буфер FIFO"**, то у нас должен быть какой-то контейнер заданного размера (раз уж *циклический*), в который по очереди добавляются элементы. Если контейнер заполнен, то первый (самый старый) элемент удаляется, первым становится следующий и тд, а новый оказывается в конце. Спойлер: решил сделать 3 показательных класса.

### 1 функция:
Иницивлизируем размер и хранилище в виде списка. В функции добавления проверяем, разолнен ли буфер, если да, то удаляем нулевой элемент, затем в любом случае добавляем новый в конец. Индексация изменяется, в прошлом первый элемент стал нулевым и тд. Функция удаления проста: если что-то есть, удаляем нулевой.

**Плюсы и минусы:** Просто, понятно. Добавление элемента происходит за O(1), а вот удаление за O(n).

### 2 функция:
Здесь исправлено то, что добавление элемента происходит за O(1) за счёт того, что теперь нет удаления элемента. Мы просто запоминаем, на какую позицию был добавлен последний элемент, чтобы на следующую позицию (а она циклически сама изменяется благодаря целочисленному делению) записывать просто новый, не удаляя старый. А для получения элемента, мы просто получаем элемент также по индексу, который запоминается.

**Плюсы и минусы:** Просто, понятно. Добавление элемента происходит за O(1) и перезаписывает старые элементы, получение элемента происходит за O(1). Однако, если понадобится добавить функцию удаления, то всё равно удалять будем за O(n). Без удаления мы конечно можем и так всё хранить и получать удобно, но из-за этого наш буфер будет только увеличиваться в размере до максимального и далее будет висеть в памяти большим размером.

### 3 функция:
Различие в том, что использована `from collections import deque`. Это позволило нам использовать `popleft()`, который удаляет элементы тоже за O(1).

**Плюсы и минусы:** Просто, понятно, но с библиотекой. Добавление элемента происходит за O(1), удаление тоже за O(1). Также добавлена проверка на заполненность и пустоту.


## Test 3
Предисловие.
Здесь всё зависит от количества элементов и их расположения, поскольку при разных входных данных разные способы сортировки могут быть противоположными по эффективности (в одном случае лучше одна, в другом - другая), а ведь ещё и тип данных важен, но у нас числа. Поскольку нас не интересует выделенная память в данной задаче (сложность по пространству), можно оценивать асимптоматику по Ω(n), Θ(n) и O(n). Внутри Python в `list.sort()` уже довольно эффективная сортировка, которая называется Timsort. Чтобы не изобретать велосипед и не описывать её заново (у нас уже есть `.sort()`), я покажу сортировку, которая отчасти реализована внутри **Timsort**. Это **сортировка слиянием**. И хоть на небольшом количестве элементов её эффективность сомнительна (как и у быстрой сортировки на стратегии "Разделяй и властвуй"), но всё же она эффективна в среднем и на большом разных чисел.
