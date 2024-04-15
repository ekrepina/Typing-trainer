# Клавиатурный тренажер
## Описание
Это программа для улучшения навыков и тренировки скорости печати.
## Функционал
* строка с отображением корректности печатания букв
* выбор языка/словаря для тренировки
* выбор темы интерфейса
* выбор количества слов в тексте
* отображение количества ошибок и скорости печати (wpm)
## Архитектура
* class Window (графический интерфейс):
  - используем библиотеку `pygame`
  - используем библиотеку `time`
  - text : Text (строка для отображения)
  - screen : pygame.display (окно вывода)
  - settings : Settings (настройки)
  - statistics : Statistics (статистика)
  - theme_button : Button (кнопка темы)
  - dict_button : Button (кнопка словаря)
  - words_button : Button (кнопка количества слов)
  - draw (вывод окна)
  - draw_text (вывод текста)
  - draw_start_text (вывод названия приложения и управления)
  - draw_statistics (вывод статистики печати)
  - input_text (обработка вводимого текста)
  - check_key (проверка корректности введенного символа)
  - update_text (обновление цвета текста)
* class Statistics (сохранение статистики):
  - time : int (время печати)
  - errors_count : int (количество ошибок)
  - wpm (количество слов в минуту)
  - update_wpm (подсчет wpm для текущей сессии)
* class Settings (хранение настроек):
  - lang : bool (язык текста)
  - theme : str (текущая тема)
  - dictionary : str (используемый словарь)
  - load_dict (загрузка файлов со словарями)
  - generate_text (генерация строки)
* class Keys (обработка нажатия кнопок клавиатуры):
  - input_key : str (введенный знак)
  - pressed_ecs (выход)
  - pressed_enter (новая строка)
  - pressed_tab (повтор строки)
  - check_key (проверка правильности текущего знака)
* class ButtonTheme (кнопка темы)
  - theme : bool (тема) 
  - image : pygame.image (значок кнопки)
  - x : int (координата по x)
  - y : int (координата по y)
  - width : int (ширина кнопки)
  - height : int (высота кнопки)
  - draw_button (вывод кнопки)
  - is_pressed (проверка нажатия на кнопку)
* class ButtonDict (кнопка словаря)
  - theme : bool (тема) 
  - lang : str (язык) 
  - text : pygame.font.Font().render() (текст кнопки)
  - x : int (координата по x)
  - y : int (координата по y)
  - width : int (ширина кнопки)
  - height : int (высота кнопки)
  - color : tuple (цвет кнопки)
  - draw_button (вывод кнопки)
  - is_pressed (проверка нажатия на кнопку)
  - change_lang (смена языка)
  - change_color (смена цвета в зависимости от темы)
* class ButtonWordCount (кнопка слов)
  - theme : bool (тема) 
  - count : str (количество слов) 
  - text : pygame.font.Font().render() (текст кнопки)
  - x : int (координата по x)
  - y : int (координата по y)
  - width : int (ширина кнопки)
  - height : int (высота кнопки)
  - color : tuple (цвет кнопки)
  - draw_button (вывод кнопки)
  - is_pressed (проверка нажатия на кнопку)
  - change_count (смена языка)
  - change_color (смена цвета в зависимости от темы)
* class Letter (отображаемая буква):
  - letter : str (буква)
  - color : str (цвет буквы в зависимости от правильности введения)

## Запуск программы

```
git clone https:/github.com/ekrepina/Typing-trainer typing-trainer
cd typing-trainer
pip install -r requirements.txt.
python main.py
```
