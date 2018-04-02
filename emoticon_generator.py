from random import choice


eye = [';', ':', '>:','>;']
nose = ['-', '+', '^']
mouth = [')', '(', 'P', '/', 'X']

i = 5
while i > 0:
    eye_rand =  choice(eye)
    nose_rand = choice(nose)
    mouth_rand = choice(mouth)
    print(eye_rand, nose_rand, mouth_rand)
    i = i - 1
