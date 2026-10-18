#!/usr/bin/env python3
"""Build the public Innernote site. No dependencies or network requests."""
from html import escape
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).resolve().parent / 'docs'
ORIGIN = 'https://innernote.ru'
EMAIL = 'ar.ar.matevosian@gmail.com'
UPDATED = '18 октября 2026 года'


def mail(subject, body=''):
    result = f'mailto:{EMAIL}?subject={quote(subject, safe="")}'
    if body:
        result += '&body=' + quote(body, safe='')
    return escape(result, quote=True)


DELETE_MAIL = mail('Удаление аккаунта Innernote', 'Здравствуйте!\n\nПрошу удалить мой аккаунт Innernote и связанные с ним облачные данные.\nEmail аккаунта: [укажите адрес]\n\nЭто письмо желательно отправить с адреса аккаунта. Пароль и записи дневника прикладывать не нужно.\n')
SUPPORT_MAIL = mail('Поддержка Innernote')


def shell(title, description, route, body):
    prefix = '../' if route else './'
    canonical = ORIGIN + ('/' + route + '/' if route else '/')
    active = lambda target: ' aria-current="page"' if route == target else ''
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="referrer" content="no-referrer">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self'; font-src 'self'; base-uri 'none'; form-action 'none'; upgrade-insecure-requests">
  <meta name="theme-color" content="#faf9fe">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:site_name" content="Innernote">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{canonical}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="{prefix}assets/logo.png" type="image/png">
  <link rel="apple-touch-icon" href="{prefix}assets/logo.png">
  <link rel="stylesheet" href="{prefix}assets/site.css">
  <title>{escape(title)}</title>
</head>
<body>
  <a class="skip" href="#main">Перейти к содержанию</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{prefix}" aria-label="Innernote — главная"><img src="{prefix}assets/logo.png" width="48" height="48" alt=""><span>Innernote</span></a>
      <nav class="site-nav" aria-label="Главная навигация">
        <a href="{prefix}#tools">Возможности</a>
        <a href="{prefix}privacy/"{active('privacy')}>Конфиденциальность</a>
        <a href="{prefix}support/"{active('support')}>Поддержка</a>
      </nav>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-main">
        <a class="brand" href="{prefix}" aria-label="Innernote — главная"><img src="{prefix}assets/logo.png" width="38" height="38" alt="" loading="lazy"><span>Innernote</span></a>
        <nav class="footer-links" aria-label="Информация о приложении">
          <a href="{prefix}privacy/">Конфиденциальность</a>
          <a href="{prefix}delete-account/">Удаление аккаунта</a>
          <a href="{prefix}support/">Поддержка</a>
        </nav>
      </div>
      <div class="footer-meta"><p>© 2026 Innernote</p><p>Инструменты самонаблюдения на основе принципов КПТ. Innernote не ставит диагнозы, не является медицинским изделием и не заменяет помощь специалиста.</p></div>
    </div>
  </footer>
</body>
</html>
'''


home = '''
  <div class="wrap">
    <section class="hero" aria-labelledby="hero-title">
      <div>
        <p class="eyebrow">Для Android · Русский и English</p>
        <h1 id="hero-title">Мысли, эмоции<br>и немного<br>больше ясности.</h1>
        <p class="lead">Innernote — дневник настроения и мыслей с инструментами КПТ. Замечай своё состояние, разбирай сложные ситуации и сохраняй то, что помогает.</p>
        <div class="hero-actions"><a class="button" href="#tools">Что внутри <span aria-hidden="true">↗</span></a><a class="text-link" href="./privacy/">Как хранятся данные</a></div>
        <p class="small-note">Основной дневник и практики доступны без аккаунта и сети.</p>
        <p style-placeholder="removed" class="small-note"><span class="availability">Готовимся к публикации в Google Play</span></p>
      </div>
      <figure class="hero-visual">
        <div class="phone"><img src="./assets/app-home.png" width="945" height="1731" alt="Главный экран Innernote: отметка настроения и начало записи СМЭР" fetchpriority="high"></div>
        <figcaption class="float-label"><strong>В своём темпе</strong>Короткая отметка.<br>Одна мысль.<br>Небольшой шаг.</figcaption>
      </figure>
    </section>
    <section class="section" id="tools" aria-labelledby="tools-title">
      <div class="section-heading"><h2 id="tools-title">Столько внимания,<br>сколько нужно тебе.</h2><p>От быстрой отметки настроения до подробного разбора мысли. Выбирай инструмент под своё состояние.</p></div>
      <div class="tool-grid">
        <article class="tool large"><span class="number">01 / ДНЕВНИК</span><h3>Понять, что произошло и что ты почувствовал.</h3><p>Запись СМЭР связывает ситуацию, мысли, эмоции и реакции. Можно вернуться к записи позже, дополнить её и провести КПТ-разбор.</p><img src="./assets/journal.webp" alt="" width="678" height="768" loading="lazy"></article>
        <article class="tool blue"><span class="number">02 / НАСТРОЕНИЕ</span><h3>Заметить, как ты сегодня.</h3><p>Отметь состояние, эмоции и жизненные контексты. История и аналитика помогут вернуться к этим наблюдениям.</p></article>
        <article class="tool mint"><span class="number">03 / ОПОРА</span><h3>Найти подходящий следующий шаг.</h3><p>Практики «Мне сейчас тяжело», карточки поддержки, экспозиции и репетиция разговора — рядом, когда хочется разобраться или подготовиться.</p></article>
      </div>
      <p class="more-tools">Также внутри: подготовка к встрече с психологом, PDF-отчёты и резервные копии. ИИ можно подключать по собственному запросу.</p>
    </section>
    <section class="section" aria-labelledby="insights-title">
      <div class="insights">
        <div><p class="eyebrow">Наблюдать за собой</p><h2 id="insights-title">Увидеть больше,<br>чем один трудный день.</h2><p>Аналитика собирает отметки настроения и результаты разбора мыслей в понятную картину. Без догадок о тех днях, когда ты ничего не записывал.</p><ul><li>Возвращайся к своим отметкам и наблюдениям.</li><li>Сравнивай состояние до и после разбора.</li><li>Выбирай, что включить в подготовку к встрече со специалистом.</li></ul></div>
        <figure><div class="phone"><img src="./assets/app-insights.png" width="840" height="1731" alt="Пример аналитики Innernote с графиком отметок настроения" loading="lazy"></div><figcaption class="caption">Экран приложения с демонстрационными данными</figcaption></figure>
      </div>
    </section>
    <section class="section" aria-labelledby="privacy-title">
      <div class="section-heading"><h2 id="privacy-title">Ты выбираешь,<br>чем делиться.</h2><p>Аккаунт, облачная синхронизация и ИИ добавляют возможности. Для ведения основного дневника они не обязательны.</p></div>
      <div class="privacy-grid">
        <article class="privacy-item"><span class="symbol" aria-hidden="true">⌂</span><h3>Сначала на устройстве</h3><p>Записи сохраняются локально. Можно включить блокировку приложения биометрией или кодом устройства.</p></article>
        <article class="privacy-item"><span class="symbol" aria-hidden="true">↗</span><h3>Облако с аккаунтом</h3><p>При входе доступна синхронизация поддерживаемых записей. История настроения остаётся на устройстве.</p></article>
        <article class="privacy-item"><span class="symbol" aria-hidden="true">✧</span><h3>ИИ по твоему запросу</h3><p>Для ответа передаётся контекст выбранного инструмента. Согласие на отправку текста можно отозвать в настройках.</p></article>
      </div>
      <a class="text-link" href="./privacy/">Подробнее об обработке данных <span aria-hidden="true">↗</span></a>
    </section>
    <section class="section" aria-labelledby="faq-title">
      <div class="faq-layout"><div><p class="eyebrow">Перед началом</p><h2 id="faq-title">Несколько<br>простых ответов.</h2><p class="small-note">Если вопрос остался, напиши в <a href="./support/">поддержку Innernote</a>.</p></div>
        <div class="faq-list">
          <details><summary>Нужно ли создавать аккаунт?</summary><div class="faq-answer">Нет. Основной дневник и локальные практики доступны без аккаунта. Вход нужен для облачной синхронизации и возможностей ИИ.</div></details>
          <details><summary>Можно ли пользоваться без интернета?</summary><div class="faq-answer">Да, локальные записи и практики работают без сети. Подключение нужно для синхронизации, служебных писем и обращения к ИИ.</div></details>
          <details><summary>Innernote заменяет психолога?</summary><div class="faq-answer">Нет. Это инструмент самонаблюдения и работы с записями. Он не ставит диагнозы и не заменяет профессиональную помощь. Ответы ИИ могут ошибаться.</div></details>
          <details><summary>Как удалить аккаунт и записи?</summary><div class="faq-answer">Облачный аккаунт удаляется в профиле приложения или по запросу через <a href="./delete-account/">эту страницу</a>. Для локальных данных предусмотрено отдельное действие в настройках.</div></details>
        </div>
      </div>
    </section>
    <section class="closing" aria-labelledby="release-title"><h2 id="release-title">Innernote скоро<br>появится в Google Play.</h2><p>Пока здесь можно узнать о возможностях приложения, обработке данных и способах связаться с разработчиком.</p><a class="button light" href="./support/">Связаться с поддержкой <span aria-hidden="true">↗</span></a></section>
  </div>
'''.replace(' style-placeholder="removed"', '')

privacy_sections = [
('about', '1. О приложении и контактах', f'''
<p>Эта политика описывает обработку данных в приложении Innernote (СМЭР) для Android и на сайте innernote.ru. Она относится к нативной версии приложения 3.0 и последующим обновлениям с описанными функциями.</p>
<p>Разработчик проекта: <strong>Innernote / MarkoDurangDurango</strong>. Контакт по вопросам конфиденциальности, доступа и удаления данных: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>Записи о состоянии, эмоциях и жизненных ситуациях могут содержать чувствительную информацию. Ты сам выбираешь, что записывать и что передавать при использовании дополнительных функций.</p>'''),
('local', '2. Данные на устройстве', '''
<p>Основные записи дневника, КПТ-разборы, экспозиции, карточки поддержки, подготовка к встрече, профиль, настройки и черновики сначала сохраняются на устройстве. История настроения хранится локально и не отправляется в Firestore.</p>
<p>Для основного дневника и локальных практик не требуется аккаунт. Временные ответы в практиках «Мне сейчас тяжело» и репетиции разговора не включаются в резервные копии и синхронизацию; они очищаются при завершении соответствующего сценария, если пользователь не сохранил результат отдельным действием.</p>
<p>Блокировка приложения использует системную биометрию или код устройства. Innernote не получает биометрический шаблон или код. Блокировка ограничивает доступ к интерфейсу, а не добавляет отдельное шифрование ко всем записям.</p>'''),
('cloud', '3. Аккаунт и облачная синхронизация', '''
<p>При создании аккаунта Firebase Authentication обрабатывает email, пароль и сведения об авторизации. Пароль передаётся службе Firebase Authentication; он не включается в дневник или служебные письма.</p>
<p>После входа поддерживаемые документы профиля, дневника СМЭР, экспозиций, карточек и подготовки к встрече могут синхронизироваться через Cloud Firestore. Это нужно для восстановления и использования данных на нескольких устройствах. Смена аккаунта не приводит к автоматической загрузке локального дневника прежнего аккаунта в новый аккаунт.</p>
<p>Firebase App Check с Play Integrity и токены авторизации используются для проверки экземпляра приложения, вошедшего пользователя и защиты серверных функций от злоупотреблений. Поставщики получают необходимые технические сведения в соответствии со своими условиями.</p>'''),
('ai', '4. Возможности ИИ', '''
<p>ИИ запускается по действию пользователя после согласия на передачу выбранного текста. Запрос проходит через сервер Innernote в Cloudflare и обрабатывается Cloudflare Workers AI. Состав отправляемых данных зависит от инструмента:</p>
<ul><li>Для расширенного разбора — выбранная запись и до двух похожих прошлых записей, выбранных локально.</li><li>Для диалога по записи — выбранная запись и ограниченная история текущего диалога, до 20 последних сообщений.</li><li>Для формулировки карточки — текст карточки и связанная исходная запись, если она есть.</li><li>Для поддержки в трудный момент — ответы выбранной практики, оценка состояния, уже испробованные подходы и текущий временный разговор.</li><li>Для репетиции разговора — ситуация, необязательные детали и до 12 реплик текущей сцены.</li></ul>
<p>Эти функции не передают весь дневник автоматически. Подбор персонализированных идей экспозиций выполняется локально. Согласие на использование ИИ можно отозвать в настройках приложения.</p>
<p>В поддерживаемых экранах можно отправить жалобу на ответ ИИ. В аккаунте сохраняются причина, необязательный комментарий, технические сведения о модели и время обращения. Исходная запись автоматически к жалобе не прикладывается. Текст ответа добавляется только при отдельном выборе пользователя; сам ответ при этом может содержать цитаты из записи.</p>'''),
('email', '5. Подтверждение email и восстановление доступа', '''
<p>Служебные письма отправляются через Resend. Этот поставщик обрабатывает адрес получателя, текст служебного письма, одноразовую ссылку Firebase и технические сведения доставки. Записи дневника, настроение и ИИ-переписка в эти письма не включаются.</p>
<p>Запросы обрабатываются сервером Innernote в Cloudflare. Временная очередь может содержать UID или email, IP запроса восстановления и подготовленное письмо со ссылкой. Записи удаляются после успешной или окончательно неуспешной обработки; также предусмотрено истечение срока очереди через 30 минут с последующей очисткой обработчиком. Служебные необратимые ключи ограничений отправки и защиты от повторов имеют срок действия до 48 часов и очищаются сервером.</p>
<p>При смене пароля на странице Innernote новый пароль передаётся напрямую в Firebase Authentication. Почтовый сервер Innernote и Resend его не получают.</p>
<p>На дату обновления этой политики стандартные тарифы Resend предусматривают 30-дневное хранение данных писем и журналов сервиса. Подробности и актуальные условия доступны в <a href="https://resend.com/security/gdpr">описании обработки данных Resend</a>.</p>'''),
('export', '6. Экспорт, виджеты и системные функции', '''
<p>JSON-копии, PDF-отчёты и изображения карточек создаются на устройстве. При сохранении файла или использовании системного меню «Поделиться» пользователь сам выбирает место хранения, приложение и получателя. Созданные файлы могут содержать личные данные.</p>
<p>Настройки виджетов позволяют включить отображение личного текста на рабочем столе. Такой текст может быть виден другим людям, имеющим доступ к экрану устройства. Голосовой ввод использует системную службу распознавания речи Android, которая может обрабатывать данные по условиям своего поставщика.</p>
<p>В нативной версии отключены автоматическое резервное копирование и перенос данных средствами Android. При переходе со старой версии приложения исходные локальные данные и неизвестные поля сохраняются в приватном миграционном архиве; он входит в пользовательский JSON-экспорт и удаляется при удалении локальных данных.</p>'''),
('website', '7. Сайт и обращения в поддержку', f'''
<p>Информационный сайт размещён на GitHub Pages. На сайте нет форм входа, оплаты или ввода дневника. Мы не подключаем к нему рекламные пиксели и стороннюю веб-аналитику. Изображения, стили и шрифт загружаются с самого сайта.</p>
<p>При посещении GitHub Pages IP-адрес посетителя регистрируется и хранится GitHub для целей безопасности. Подробнее — в <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">политике конфиденциальности GitHub</a>.</p>
<p>Кнопки связи открывают почтовую программу. Отправка происходит после действия пользователя в этой программе. Поддержка получает адрес отправителя, текст и добровольно приложенные файлы. Переписка сохраняется в почтовом ящике поддержки до её удаления; запросить удаление своего обращения можно по адресу <a href="mailto:{EMAIL}">{EMAIL}</a>. Для обычного обращения не нужно присылать пароль или содержимое дневника.</p>'''),
('retention', '8. Сроки хранения и удаление', '''
<ul><li><strong>Локальные записи и архив переноса:</strong> хранятся на устройстве до удаления через настройки приложения или очистки данных приложения средствами Android.</li><li><strong>Облачные документы:</strong> хранятся, пока пользователь сохраняет аккаунт; удаляются из рабочего хранилища при удалении аккаунта.</li><li><strong>Временные разговоры:</strong> очищаются при выходе из соответствующего сценария, если результат не был отдельно сохранён.</li><li><strong>Очередь служебных писем:</strong> удаление после обработки либо по истечении 30 минут при очистке очереди; ключи ограничений отправки — до 48 часов.</li><li><strong>Данные писем и журналы Resend:</strong> стандартный срок на дату политики — 30 дней.</li><li><strong>Экспортированные файлы:</strong> остаются там, куда их сохранил пользователь, и удаляются им самостоятельно.</li></ul>
<p>Google указывает, что IP-адреса в журналах Firebase Authentication хранятся несколько недель, а удаление прочих данных авторизации из рабочих и резервных систем провайдера завершается в течение 180 дней после удаления пользователя разработчиком. Это срок очистки систем поставщика, а не сохранение возможности входа в удалённый аккаунт. Источник: <a href="https://firebase.google.com/support/privacy">данные о конфиденциальности Firebase</a>.</p>
<p>Удаление аккаунта удаляет Firebase Authentication account, облачный профиль, синхронизированные записи, экспозиции, карточки, подготовку к встрече и AI-жалобы. Локальный дневник при этом сохраняется и удаляется отдельным действием. Удаление приложения с телефона само по себе не удаляет аккаунт и данные в облаке.</p>
<p>Запросить удаление аккаунта можно в приложении или без его установки на <a href="../delete-account/">странице удаления аккаунта</a>. Служебные данные поставщиков, не относящиеся к рабочим документам аккаунта, могут обрабатываться ими в течение сроков, установленных их условиями.</p>'''),
('providers', '9. Поставщики услуг и передача данных', '''
<p>Для описанных функций используются следующие поставщики:</p>
<ul><li><a href="https://firebase.google.com/support/privacy">Google Firebase</a> — авторизация, синхронизация и защита доступа к серверным функциям.</li><li><a href="https://www.cloudflare.com/privacypolicy/">Cloudflare</a> и <a href="https://developers.cloudflare.com/workers-ai/platform/data-usage/">Cloudflare Workers AI</a> — серверная обработка запросов и выбранного контекста для ИИ.</li><li><a href="https://resend.com/legal/privacy-policy">Resend</a> — доставка служебных писем.</li><li><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub</a> — размещение информационного сайта.</li></ul>
<p>Обработка у поставщиков может выполняться за пределами страны пользователя. Доступ, служебные журналы, резервирование и сроки хранения у поставщиков регулируются их условиями. Передача данных серверным функциям приложения осуществляется через HTTPS.</p>'''),
('choices', '10. Твои возможности и изменения политики', f'''
<p>Можно пользоваться основным дневником без аккаунта, отозвать согласие на ИИ, экспортировать свои записи, удалить локальные данные или запросить удаление облачного аккаунта. По вопросам доступа, исправления или удаления данных напиши на <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>При изменениях в работе приложения эта страница обновляется. Дата актуальной редакции указана в начале. Возможности ИИ не являются медицинской консультацией; их ответы могут содержать ошибки.</p>'''),
]

privacy_toc = '<aside class="contents" aria-label="Содержание политики"><strong>На этой странице</strong><ol>' + ''.join(f'<li><a href="#{key}">{escape(title[title.find(".") + 2:])}</a></li>' for key, title, _ in privacy_sections) + '</ol></aside>'
privacy_body = f'''
<div class="wrap document">
  <p class="breadcrumbs"><a href="../">Главная</a> / Конфиденциальность</p>
  <header class="document-intro"><h1>Политика конфиденциальности Innernote</h1><p class="lead">Какие данные остаются на устройстве, что передаётся при дополнительных функциях и как управлять своими записями.</p><p class="date">Обновлено: {UPDATED}</p></header>
  <div class="document-grid">{privacy_toc}<article class="prose">''' + ''.join(f'<section id="{key}" aria-labelledby="{key}-title"><h2 id="{key}-title">{escape(title)}</h2>{content}</section>' for key, title, content in privacy_sections) + '</article></div></div>'

delete_body = f'''
<div class="wrap document">
  <p class="breadcrumbs"><a href="../">Главная</a> / Удаление аккаунта</p>
  <header class="document-intro"><h1>Удаление аккаунта Innernote</h1><p class="lead">Здесь можно запросить удаление аккаунта и связанных облачных данных. Для этого не нужно устанавливать приложение или входить в него.</p></header>
  <div class="wide-prose">
    <section class="action-panel" aria-labelledby="request-title"><h2 id="request-title">Отправить запрос разработчику</h2><p>Напиши с email, на который зарегистрирован аккаунт Innernote. Укажи, что хочешь удалить аккаунт и все связанные облачные данные.</p><a class="button" href="{DELETE_MAIL}">Запросить удаление по email <span aria-hidden="true">↗</span></a><p class="small-note">Откроется твоя почтовая программа. Письмо нужно отправить из неё.</p><p class="email"><a href="mailto:{EMAIL}">{EMAIL}</a></p></section>
    <article class="prose">
      <section aria-labelledby="delete-next"><h2 id="delete-next">Как обрабатывается запрос</h2><ol class="steps"><li>Отправь письмо с темой <strong>«Удаление аккаунта Innernote»</strong> с адреса своего аккаунта.</li><li>Разработчик проверит, что аккаунт принадлежит тебе. Если потребуется уточнение, оно придёт на этот адрес. Пароль и записи дневника для запроса не нужны.</li><li>После проверки будут удалены аккаунт и связанные данные в рабочем облачном хранилище. О завершении сообщим ответным письмом.</li></ol><p>Если доступа к адресу аккаунта больше нет, напиши об этом в запросе. Понадобится дополнительная проверка принадлежности аккаунта.</p></section>
      <section aria-labelledby="delete-what"><h2 id="delete-what">Что удаляется, а что остаётся</h2><div class="table-scroll" role="region" aria-label="Данные при удалении аккаунта" tabindex="0"><table><thead><tr><th scope="col">Данные</th><th scope="col">Что происходит</th></tr></thead><tbody>
        <tr><td>Учётная запись и облачный профиль</td><td>Удаляются. Войти в этот аккаунт после удаления нельзя.</td></tr>
        <tr><td>Облачные записи СМЭР, экспозиции, карточки, подготовка к встрече и AI-жалобы</td><td>Удаляются из рабочего хранилища аккаунта.</td></tr>
        <tr><td>Локальный дневник и история настроения на телефоне</td><td>Остаются на устройстве. Их можно отдельно удалить в настройках приложения.</td></tr>
        <tr><td>Сохранённые JSON, PDF и изображения</td><td>Остаются в выбранных тобой папках и сервисах. Их нужно удалить самостоятельно.</td></tr>
        <tr><td>Технические копии данных авторизации у Firebase</td><td>Google указывает срок очистки рабочих и резервных систем Authentication до 180 дней после удаления пользователя. Доступ в удалённый аккаунт прекращается; подробности приведены в политике конфиденциальности.</td></tr>
        <tr><td>Служебные сведения доставки писем</td><td>Очередь Innernote очищается после обработки или по истечении 30 минут; ключи ограничений — до 48 часов. Resend хранит данные писем и журналы до 30 дней на стандартных тарифах.</td></tr>
      </tbody></table></div><p>Переписку с поддержкой можно также попросить удалить. Подробнее о данных поставщиков — в <a href="../privacy/#retention">политике конфиденциальности</a>.</p></section>
      <section aria-labelledby="delete-app"><h2 id="delete-app">Удалить аккаунт в приложении</h2><ol class="steps"><li>Открой <strong>«Профиль» → «Облачный аккаунт»</strong>.</li><li>Выбери <strong>«Удалить аккаунт»</strong>, введи текущий пароль и подтверди удаление.</li><li>Для удаления данных с телефона открой <strong>«Настройки и приватность» → «Удалить локальные данные»</strong>.</li></ol><div class="notice blue"><strong>Удаление приложения не удаляет облачный аккаунт.</strong><p>Если приложение уже удалено, используй запрос по email выше. Повторная установка не требуется.</p></div></section>
    </article>
  </div>
</div>'''

support_faqs = [
('Не пришло письмо подтверждения. Что делать?', 'Проверь папки «Спам» и «Промоакции». В облачном профиле можно выбрать «Отправить письмо подтверждения». Если только что запросил письмо, подожди не меньше минуты перед повтором. Если письма нет, напиши в поддержку с адреса своего аккаунта.'),
('Подтвердил email, а приложение ещё просит подтвердить.', 'Вернись в облачный профиль Innernote и нажми «Проверить подтверждение». Переход по ссылке в письме сам по себе не обновляет уже открытый экран приложения.'),
('Как восстановить пароль?', 'На экране входа введи email аккаунта и выбери «Сбросить пароль по email». Открой служебное письмо и задай новый пароль на странице восстановления. Для защиты адресов приложение может показать одинаковый ответ и для неизвестного email.'),
('Как перенести записи на другой телефон?', 'Можно сохранить JSON-копию через «Настройки и приватность» → «Экспортировать данные», а затем импортировать её на новом устройстве. Для поддерживаемых записей также доступна облачная синхронизация после входа. История настроения остаётся локальной и переносится с резервной копией.'),
('Как удалить аккаунт без приложения?', 'Открой <a href="../delete-account/">страницу удаления аккаунта</a> и отправь запрос с email своего аккаунта. На странице также описано, какие данные удаляются и как очистить данные с телефона.'),
('Как сообщить об ошибке или проблемном ответе ИИ?', 'Напиши, что произошло и в каком разделе, укажи версию Innernote и Android. В поддерживаемых экранах можно отправить жалобу непосредственно на ответ ИИ. Не прикладывай пароли и приватные записи без необходимости; на скриншоте можно предварительно скрыть личную информацию.'),
]

support_body = f'''
<div class="wrap document">
  <p class="breadcrumbs"><a href="../">Главная</a> / Поддержка</p>
  <header class="document-intro"><h1>Поддержка Innernote</h1><p class="lead">Вопросы о приложении, доступе к аккаунту и работе с данными можно отправить разработчику.</p></header>
  <div class="support-layout">
    <section class="action-panel" aria-labelledby="contact-title"><h2 id="contact-title">Написать разработчику</h2><p>Опиши, что произошло. Для технической проблемы помогут версия приложения, версия Android и название раздела.</p><a class="button" href="{SUPPORT_MAIL}">Открыть письмо <span aria-hidden="true">↗</span></a><p class="email"><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="small-note">Пароль от аккаунта и содержимое дневника для обычного обращения не нужны.</p></section>
    <section class="faq-list" aria-label="Частые вопросы">''' + ''.join(f'<details><summary>{escape(q)}</summary><div class="faq-answer">{a}</div></details>' for q, a in support_faqs) + '''</section>
  </div>
  <div class="support-foot prose"><p>По вопросам конфиденциальности и удаления данных можно обратиться на тот же адрес. <a href="../privacy/">Политика конфиденциальности</a> · <a href="../delete-account/">Удаление аккаунта</a>.</p><p>Поддержка Innernote отвечает на вопросы о приложении и не оказывает медицинскую помощь.</p></div>
</div>'''

pages = [
('', 'Innernote — дневник мыслей и настроения', 'Дневник настроения и мыслей, КПТ-разбор, практики самопомощи и карточки поддержки для Android. Основные функции доступны без аккаунта.', home),
('privacy', 'Политика конфиденциальности — Innernote', 'Как Innernote хранит записи, использует облачную синхронизацию, ИИ и служебные письма. Контакты и способы удаления данных.', privacy_body),
('delete-account', 'Удаление аккаунта и данных — Innernote', 'Запросить удаление аккаунта Innernote и связанных облачных данных без установки приложения. Инструкции и контакт разработчика.', delete_body),
('support', 'Поддержка — Innernote', 'Связаться с разработчиком Innernote. Восстановление доступа, подтверждение email, резервные копии и удаление аккаунта.', support_body),
]

for route, title, description, body in pages:
    target = OUT / route / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shell(title, description, route, body), encoding='utf-8')

# Relative links are used on normal pages, allowing both the GitHub project URL
# and the final custom domain. A 404 must also work for arbitrarily deep paths.
error_body = '<div class="wrap"><section class="error-page"><p class="eyebrow">Страница не найдена · 404</p><h1>Здесь пока нет записи.</h1><p>Возможно, ссылка изменилась. На главной есть информация об Innernote, контакты и страницы управления данными.</p><a class="button" href="https://innernote.ru/">На главную</a></section></div>'
error_page = shell('Страница не найдена — Innernote', 'Эта страница Innernote не найдена.', '', error_body)
error_page = error_page.replace('href="./', 'href="https://innernote.ru/').replace('src="./', 'src="https://innernote.ru/')
error_page = error_page.replace('<link rel="canonical" href="https://innernote.ru/">', '<meta name="robots" content="noindex">')
(OUT / '404.html').write_text(error_page, encoding='utf-8')
(OUT / '.nojekyll').write_text('', encoding='utf-8')
(OUT / 'CNAME').write_text('innernote.ru\n', encoding='utf-8')
(OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://innernote.ru/sitemap.xml\n', encoding='utf-8')
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for route, *_ in pages:
    sitemap += '  <url><loc>' + ORIGIN + ('/' + route + '/' if route else '/') + '</loc><lastmod>2026-10-18</lastmod></url>\n'
(OUT / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
print(f'Built {len(pages)} pages and 404 in {OUT}')
