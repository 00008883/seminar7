csf = {
    'cw1-weight': 0.4,
    'cw1-mark': 79,
    'exam-weight': 0.6,
    'exam-mark': 65
}

mark1 = csf.get('cw1-mark') * csf.get('cw1-weight');
mark2 = csf.get('exam-mark') * csf.get('exam-weight');

result = mark1 + mark2;
print('Your result is: ' + str(result));