import speech_recognition as sr
from gtts import gTTS
from playsound3 import playsound
from g4f.client import Client
import os
from random import randint


def start():
    # Получаем имя пользователя
    username = os.getlogin()




    browser = 'firefox'
    client = Client()


    def speak(text):
        tts = gTTS(text, lang='ru')
        tts.save('text.mp3')
        playsound('text.mp3')

    class VoiceAssistant:
        def __init__(self):
            self.recognizer = sr.Recognizer()

        def listen(self):
            with sr.Microphone() as source:
                print("Слушаю...")
                audio = self.recognizer.listen(source)
                try:
                    command = self.recognizer.recognize_google(audio, language='ru-RU')
                    print(f"Вы сказали: {command}")
                    return command
                except sr.UnknownValueError:
                    print("Не удалось распознать команду.")
                    return None
                except sr.RequestError:
                    print("Ошибка сервиса распознавания.")
                    return None

        def run(self):
            playsound('sounds/run.wav')
            print(f"Привет \033[31m{username}\033[0m Я ваш голосовой помощник. Чем я могу помочь сегодня.")
            while True:
                command = self.listen()
                if command:
                    if "стоп" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "хватит" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "выход" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "харэ" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "харе" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "exit" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "quit" in command.lower():
                        playsound('sounds/off.wav')
                        print("До свидания!")
                        break
                    elif "браузер" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю браузер.")
                        os.system(f'{browser}')
                    elif "ютуб" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю ютуб.")
                        os.system(f'{browser} http://youtube.com')
                    elif "youtube" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю ютуб.")
                        os.system(f'{browser} http://youtube.com')
                    elif "github" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю github.")
                        os.system(f'{browser} http://github.com')
                    elif "tiktok" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю tiktok.")
                        os.system(f'{browser} http://www.tiktok.com/')
                    elif "тикток" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю tiktok.")
                        os.system(f'{browser} http://www.tiktok.com/')
                    elif "instagram" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю instagram.")
                        os.system(f'{browser} http://www.instagram.com/')
                    elif "инстаграм" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю instagram.")
                        os.system(f'{browser} http://www.instagram.com/')
                    elif "reddit" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю reddit.")
                        os.system(f'{browser} http://www.reddit.com/')
                    elif "редит" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю reddit.")
                        os.system(f'{browser} http://www.reddit.com/')
                    elif "vk" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю vk.")
                        os.system(f'{browser} http://vk.com/')
                    elif "вк" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю vk.")
                        os.system(f'{browser} http://vk.com/')
                    elif "discord" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю discord.")
                        os.system(f'{browser} http://discord.com/')
                    elif "дискорд" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print("Запускаю discord.")
                        os.system(f'{browser} http://discord.com/')
                    elif "молодец" in command.lower():
                        playsound(f'sounds/thanks.wav')
                    elif "сигнализац" in command.lower():
                        playsound(f'sounds/ok{randint(1,4)}.wav')
                        print('Запускаю сигнализацию.')
                        while True:
                            playsound('signalling.mp3')
                            print('Казахстан угрожает нам бомбардировкой!')
                            print('Казахстан угрожает нам бомбардировкой!')
                            print('Казахстан угрожает нам бомбардировкой!')
                            print('Казахстан угрожает нам бомбардировкой!')
                            print('Казак!')
                    else:
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[{"role": "user", "content": command}],
                                web_search=True
                            )
                            # Проверьте структуру response перед доступом к данным
                            print(response)  # Выводим ответ для проверки структуры

                            # Измените в зависимости от структуры ответа
                            if hasattr(response, 'choices') and len(response.choices) > 0:
                                response_text = response.choices[0].message.content  # Используйте точечную нотацию
                                speak(response_text)
                                print(response_text)
                                
                            else:
                                print("Нет доступных ответов.")
                                playsound('sounds/not_found.wav')
                        except Exception as e:
                            print(f"Ошибка при получении ответа: {e}")
                            speak("Извините, произошла ошибка при получении ответа.")


    assistant = VoiceAssistant()
    assistant.run()

def word_detector(target_words, exit_words):
    # Инициализация распознавателя
    recognizer = sr.Recognizer()

    # Используем микрофон как источник звука
    with sr.Microphone() as source:
        print("Слушаю... Пожалуйста, говорите.")
        while True:
            try:
                # Слушаем звук и распознаем речь
                audio = recognizer.listen(source)
                nolower_text = recognizer.recognize_google(audio, language='ru-RU')
                text = nolower_text.lower()
                print(f"Вы сказали: {text}")

                # Проверяем наличие целевых слов в распознанном тексте
                found_words = [word for word in target_words if word in text]
                
                found_words_exit = [word for word in exit_words if word in text]
                if found_words:
                    start()
                elif found_words_exit:
                    playsound('sounds/off.wav')
                    exit(0)

            except sr.UnknownValueError:
                print("Не удалось распознать речь.")
            except sr.RequestError as e:
                print(f"Ошибка сервиса распознавания: {e}")

if __name__ == "__main__":
    alias = ["jarvis", "джарвис", "джар", "jarвис", "jar", "джа"]
    quit_words = ["стоп","stop","хватит","выход", "харэ", "харе", "exit", "quit"]
    while True:
        word_detector(alias, quit_words)