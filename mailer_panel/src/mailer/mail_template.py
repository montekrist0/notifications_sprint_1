header = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>YandexPraktikum</title></head><body>'
footer = '</body></html>'

welcome = header + '<div>Спасибо за регистрацию {{user_name}}</div>' + footer
like = header + '<div>вам поставили {{likes_count_new}} лайк(-ов)</div>' + footer
personal_selection = (
    header + '<div>{{user_name}} для вас персональная рассылка</div>' + footer
)
mass = header + '<div>{{user_name}} массовая рассылка спешил фор ю</div>'
private = header + '<div>{{user_name}} {{content}}</div>'
