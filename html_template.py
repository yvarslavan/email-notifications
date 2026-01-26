#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
from html import escape

def html_footer() :
    html = '''
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
 '''
    return html

def html_contact () :
    html = '''
<!-- Блок оценки работы -->
<div style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius:12px; box-shadow:0 8px 25px rgba(0,0,0,0.15); margin:20px 0; padding:30px; text-align:center">
	<div style="background:rgba(255,255,255,0.95); border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); padding:25px">
		<h3 style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:18px; font-weight:600; margin-bottom:25px; text-shadow:0 1px 2px rgba(0,0,0,0.1)">Оцените, пожалуйста, нашу работу по задаче</h3>

												<div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin-bottom:15px;">
			<div style="text-align:center;">
				<a href="https://helpdesk.teztour.com/Contact/" style="background:linear-gradient(135deg, #4CAF50 0%, #45a049 100%); border-radius:50%; box-shadow:0 6px 20px rgba(76, 175, 80, 0.4); display:inline-block; padding:0; text-decoration:none; transition:all 0.3s ease; border:3px solid rgba(255,255,255,0.3); width:70px; height:70px; text-align:center; line-height:70px; font-size:32px;">
					&#128522;
				</a>
				<div style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:12px; font-weight:600; margin-top:8px;">Отлично</div>
			</div>

			<div style="text-align:center;">
				<a href="https://helpdesk.teztour.com/Contact/" style="background:linear-gradient(135deg, #FF9800 0%, #F57C00 100%); border-radius:50%; box-shadow:0 6px 20px rgba(255, 152, 0, 0.4); display:inline-block; padding:0; text-decoration:none; transition:all 0.3s ease; border:3px solid rgba(255,255,255,0.3); width:70px; height:70px; text-align:center; line-height:70px; font-size:32px;">
					&#128528;
				</a>
				<div style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:12px; font-weight:600; margin-top:8px;">Хорошо</div>
			</div>

			<div style="text-align:center;">
				<a href="https://helpdesk.teztour.com/Contact/" style="background:linear-gradient(135deg, #f44336 0%, #d32f2f 100%); border-radius:50%; box-shadow:0 6px 20px rgba(244, 67, 54, 0.4); display:inline-block; padding:0; text-decoration:none; transition:all 0.3s ease; border:3px solid rgba(255,255,255,0.3); width:70px; height:70px; text-align:center; line-height:70px; font-size:32px;">
					&#128542;
				</a>
				<div style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:12px; font-weight:600; margin-top:8px;">Плохо</div>
			</div>
		</div>

		<div style="color:#7f8c8d; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:12px; text-align:center; font-style:italic;">
			Нажмите на смайлик, чтобы оставить отзыв
		</div>
	</div>
</div>
'''
    return html

def template_html_new_issue_msk (issueID, subject, description, status, created_on) :
    # Экранируем переменные для защиты от XSS
    safe_issueID = escape(str(issueID))
    safe_subject = escape(str(subject))
    safe_description = escape(str(description))
    safe_status = escape(str(status))
    safe_created_on = escape(str(created_on))

    html= '''
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
    <table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
        <tr>
            <td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">
                <table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">

                    <!-- Стильная шапка -->
                    <tr>
                        <td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; width:100%; margin:0; padding:0;">
                                <tbody>
                                    <tr>
                                        <td style="padding: 25px 20px; text-align: left;">
                                            <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); border-radius: 8px; padding: 15px; display: inline-block; border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                                                <a href="http://www.tez-tour.com" target="_blank">
                                                    <img alt="TEZ TOUR" src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" title="TEZ TOUR" style="max-height: 50px; filter: brightness(1.2) contrast(1.1);" />
                                                </a>
                                            </div>
                                        </td>
                                        <td style="padding: 25px 20px; text-align: right;">
                                            <div style="color:#ffffff; font-family:Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:18px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                                                <strong>Служба технической поддержки TEZ TOUR</strong><br />
                                                Email: <a href="mailto:help@tez-tour.com" target="_blank" style="color: #ffffff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.5);">help@tez-tour.com</a>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>

                    <!-- Тонкая красная акцентная полоса -->
                    <tr>
                        <td style="padding: 0; margin: 0;">
                            <div style="width: 100%; height: 1px; background: linear-gradient(90deg, #e94560 0%, #ff6b6b 50%, #e94560 100%); margin: 0; padding: 0;"></div>
                        </td>
                    </tr>

                    <!-- Основной контент -->
                    <tr align="top">
                        <td bgcolor="#f1eff0" style="padding: 20px 25px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-left: 4px solid #3498db;">
                            <div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #2c3e50; line-height: 1.5;">

                                <!-- Приветствие -->
                                <div style="margin-bottom: 15px;">
                                    Здравствуйте!
                                </div>

                                <!-- Информация о регистрации -->
                                <div style="background: rgba(52, 152, 219, 0.1); border-radius: 6px; padding: 12px; margin-bottom: 15px; border-left: 3px solid #3498db;">
                                    Ваше обращение в IT-Департамент зарегистрировано в системе под номером - #<strong>''' + safe_issueID + '''</strong><br />
                                    Сохраняйте, пожалуйста, историю переписки.
                                </div>

                                <!-- Информационное сообщение -->
                                <div style="background: rgba(255, 193, 7, 0.1); border-radius: 6px; padding: 12px; margin-bottom: 15px; border-left: 4px solid #ffc107;">
                                    <p style="text-align: justify; margin: 0; color: #856404; font-size: 13px; line-height: 1.4;">
                                        <ins><small><em>Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на <a href="mailto:help@tez-tour.com" target="_blank" style="color: #856404; text-decoration: underline;">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.</em></small></ins>
                                    </p>
                                </div>

                                <!-- Ссылка на портал -->
                                <div style="background: rgba(40, 167, 69, 0.1); border-radius: 6px; padding: 12px; margin-bottom: 15px; border-left: 4px solid #28a745;">
                                    <p style="margin: 0; color: #155724; font-size: 14px; line-height: 1.4;">
                                        Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе <a href="https://its.tez-tour.com" style="color: #155724; text-decoration: underline; font-weight: 500;">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
                                    </p>
                                </div>

                                <!-- Детали заявки -->
                                <div style="background: #f8f9fa; border-radius: 6px; padding: 12px; margin-bottom: 15px; border: 1px solid #e9ecef;">
                                    <table cellspacing="0" style="width: 100%;">
                                        <tr>
                                            <td style="color: #6c757d; font-weight: 500; padding: 2px 0;"><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td>
                                            <td style="color: #2c3e50; padding: 2px 0;"><FONT size=3><strong>''' + safe_subject + '''</strong></FONT></td>
                                        </tr>
                                        <tr>
                                            <td style="color: #6c757d; font-weight: 500; padding: 2px 0;"><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td>
                                            <td style="color: #2c3e50; padding: 2px 0;"><FONT size=3><strong>''' + safe_status + '''</strong></FONT></td>
                                        </tr>
                                        <tr>
                                            <td style="color: #6c757d; font-weight: 500; padding: 2px 0;"><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td>
                                            <td style="color: #2c3e50; padding: 2px 0;"><FONT size=3><strong>''' + safe_created_on + '''</strong></FONT></td>
                                        </tr>
                                    </table>
                                </div>

                                <!-- Разделитель -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                    <tr>
                                        <td style="border-bottom: 1px solid #d1cdc7;"></td>
                                    </tr>
                                    <tr>
                                        <td style="height: 8px;">&nbsp;</td>
                                    </tr>
                                </table>

                                <!-- Описание заявки -->
                                <div style="background: #ffffff; border-radius: 6px; padding: 15px; border: 1px solid #e9ecef; margin-bottom: 15px;">
                                    <pre style="font-family: 'Segoe UI', Arial, Helvetica, sans-serif; white-space: pre-wrap; margin: 0; color: #2c3e50; font-size: 14px; line-height: 1.5;">''' + safe_description + '''</pre>
                                </div>

                                <!-- Разделитель -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                    <tr>
                                        <td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td bgcolor="#f1eff0" style="height: 8px;">&nbsp;</td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>

                    <!-- Стильный футер -->
                    <tr>
                        <td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 0; padding: 0; width: 100%;">
                                <tr>
                                    <td style="padding: 15px 25px; margin: 0;">
                                        <!-- Основная информация -->
                                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                                            <!-- Логотип и название -->
                                            <div style="display: flex; align-items: center; gap: 15px;">
                                                <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" style="max-height: 30px; width: auto; filter: brightness(1.2) contrast(1.1);" />
                                                <div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 15px; color: #ffffff; line-height: 1.4; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                                                    <span style="font-weight: 600; color: #ffffff; font-size: 16px;">Международный туроператор <strong style="color: #3498db;">TEZ TOUR</strong></span><br>
                                                    <a href="http://www.tez-tour.com" target="_blank" style="color: #3498db; text-decoration: none; font-weight: 500; transition: color 0.3s ease;">www.tez-tour.com</a>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
'''
    return html

def template_html_new_issue_ukr (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Служба технической поддержки Тез Тур Украина</b><br><a href="tel:+ 380 (44) 495-55-05">+ 380 (44) 495-55-05</a>, вн.4156/4148/4170<br>Email: <a href="mailto: it@teztour.com.ua" target="_blank">it@teztour.com.ua</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/><br/>
Ваше обращение зарегистрировано в системе под номером - #<strong>''' + issueID + '''</strong><br />
Сохраняйте, пожалуйста, историю переписки.<br />
<p style="text-align: justify;">
    <ins>
        <small>
            <em>
                Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                <a href="mailto:it@teztour.com.ua" target="_blank">it@teztour.com.ua</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
            </em>
        </small>
    </ins>
</p>
<p>
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html_new_issue_spain (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="900" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Служба технической поддержки TEZ TOUR Spain & Caribbean</b><br>Понедельник-Пятница 9:00-18:00<br>Email: <a href="mailto:help@teztour.es" target="_blank">help@teztour.es<br>Внутренний IP-номер: 4777</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/><br/>
Благодарим за Ваше обращение в службу технической поддержки Tez Tour Spain & Caribbean.<br />
Ваше обращение зарегистрировано в системе под номером - #<strong>''' + issueID + '''</strong><br />
Сохраняйте, пожалуйста, историю переписки.<br />
<p style="text-align: justify;">
    <ins>
        <small>
            <em>
                Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                <a href="mailto:help@teztour.es" target="_blank">help@teztour.es</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
            </em>
        </small>
    </ins>
</p>
<p>
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html (issueID, body, strParam, oldParam, newParam, dateCreated, author, status, priority, assigned) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">
<table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">

<!-- Стильная шапка -->
<tr>
<td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; width:100%; margin:0; padding:0;">
	<tbody>
		<tr>
			<td style="padding: 25px 20px; text-align: left;">
				<div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); border-radius: 8px; padding: 15px; display: inline-block; border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
					<a href="http://www.tez-tour.com" target="_blank">
						<img alt="TEZ TOUR" src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" title="TEZ TOUR" style="max-height: 50px; filter: brightness(1.2) contrast(1.1);" />
					</a>
				</div>
			</td>
			<td style="padding: 25px 20px; text-align: right;">
				<div style="color:#ffffff; font-family:Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:18px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
					<strong>Служба технической поддержки TEZ TOUR</strong><br />
					Email: <a href="mailto:help@tez-tour.com" target="_blank" style="color: #ffffff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.5);">help@tez-tour.com</a>
				</div>
			</td>
		</tr>
	</tbody>
</table>
</td>
</tr>

<!-- Тонкая красная акцентная полоса -->
<tr>
<td style="padding: 0; margin: 0;">
<div style="width: 100%; height: 1px; background: linear-gradient(90deg, #e94560 0%, #ff6b6b 50%, #e94560 100%); margin: 0; padding: 0;"></div>
</td>
</tr>

<!-- Стильный основной контент -->
<tr>
<td style="padding: 30px 25px; background: #ffffff; margin: 0;">
<div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #2c3e50; line-height: 1.6;">

<!-- Информационная панель -->
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; padding: 20px; margin-bottom: 25px; border-left: 4px solid #3498db; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">

<table cellspacing="0" style="width: 100%;">
   <tr>
    <td style="padding: 8px 0;"><span style="color: #e74c3c; font-weight: 600;">&bull;</span> <b style="color: #2c3e50;">''' + strParam + '''</b> изменился с <b style="color: #e67e22;">''' + oldParam + '''</b> на <b style="color: #27ae60;">''' + newParam + '''</b></td>
   </tr>
</table>
<br />
<table cellspacing="0" style="width: 100%;">
   <tr>
    <td style="padding: 6px 0; width: 120px;"><span style="color: #3498db; font-weight: 600;">&bull; Автор:</span></td><td style="padding: 6px 0; color: #2c3e50;">''' + author + '''</td>
   </tr>
   <tr>
    <td style="padding: 6px 0;"><span style="color: #3498db; font-weight: 600;">&bull; Статус:</span></td><td style="padding: 6px 0; color: #2c3e50;">''' + status + '''</td>
   </tr>
   <tr>
    <td style="padding: 6px 0;"><span style="color: #3498db; font-weight: 600;">&bull; Приоритет:</span></td><td style="padding: 6px 0; color: #2c3e50;">''' + priority + '''</td>
   </tr>
   <tr>
    <td style="padding: 6px 0;"><span style="color: #3498db; font-weight: 600;">&bull; Исполнитель:</span></td><td style="padding: 6px 0; color: #2c3e50;">''' + assigned + '''</td>
   </tr>
   <tr>
    <td style="padding: 6px 0;"><span style="color: #3498db; font-weight: 600;">&bull; Дата создания:</span></td><td style="padding: 6px 0; color: #2c3e50;">''' + dateCreated + '''</td>
   </tr>
</table>
</div>

<!-- Основной текст -->
<div style="background: #ffffff; border-radius: 8px; padding: 20px; border: 1px solid #e9ecef; margin-bottom: 25px;">
<div style="line-height: 1.6;">
    <span style="font-family: 'Segoe UI', Arial, Helvetica, sans-serif; font-size: 14px; color: #2c3e50; line-height: 1.6;">
       <pre style="font-family: inherit; white-space: pre-wrap; margin: 0; color: #34495e;">''' + body + '''</pre>
    </span>
</div>
</div>

<!-- Информационные блоки -->
<div style="background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); border-radius: 8px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #f39c12;">
<p style="text-align: justify; margin: 0; color: #856404; font-size: 13px; line-height: 1.5;">
    <em>
        Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
        <a href="mailto:help@tez-tour.com" target="_blank" style="color: #e67e22; text-decoration: none; font-weight: 600;">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
    </em>
</p>
</div>

<div style="background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%); border-radius: 8px; padding: 20px; border-left: 4px solid #17a2b8;">
<p style="margin: 0; color: #0c5460; font-size: 14px; line-height: 1.5;">
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com" style="color: #17a2b8; text-decoration: none; font-weight: 600;">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>
</div>

</div>
</td>
</tr>

<!-- Стильный футер -->
<tr>
<td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 0; padding: 0; width: 100%;">
<tr>
<td style="padding: 20px 25px; margin: 0;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 15px;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" style="max-height: 35px; width: auto; filter: brightness(1.2) contrast(1.1);" />
            <div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 16px; color: #ffffff; line-height: 1.5; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                <span style="font-weight: 600; color: #ffffff; font-size: 18px;">Международный туроператор <strong style="color: #3498db;">TEZ TOUR</strong></span><br>
                <a href="http://www.tez-tour.com" target="_blank" style="color: #3498db; text-decoration: none; font-weight: 500; transition: color 0.3s ease;">www.tez-tour.com</a>
            </div>
        </div>
    </div>
</td>
</tr>
</table>
</td>
</tr>

</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html_Ufa (issueID, body, strParam, oldParam, newParam, dateCreated, author, status, priority, assigned) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Отдел расчетов</b>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 10px 0px 10px 0px;">
<tr>
<td align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; line-height: 18px;">

<table cellspacing="0">
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;''' + ' <b>' + strParam +  '</b> изменился с <b>' + oldParam + '</b> на <b>' + newParam + '</b>' + '''</FONT></td>
   </tr>
</table>
<br />
<table cellspacing="0">
   <tr>
  <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Автор:</FONT></td><td><FONT size=2>''' + author + '''</FONT></td>
    </tr>
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=2>''' + status + '''</FONT></td>
   </tr>
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Приоритет:</FONT></td><td><FONT size=2>''' + priority + '''</FONT></td>
   </tr>
     <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Исполнитель:</FONT></td><td><FONT size=2>''' + assigned + '''</FONT></td>
   </tr>
     <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=2>''' + dateCreated  + '''</FONT></td>
   </tr>
  </table>
<div style="line-height:18px;">
    <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color:#000000;line-height:20px;">
       <pre>''' + body + ''' </pre>
    </span>
</div> <br /><br />
'''
    return html

def template_html_Assigned_Ufa (issueID, body, strParam, oldParam, newParam, dateCreated, title, author, status, priority, assigned, add_notes) :

    if add_notes != '':
        # add_notes = '<div style = "border-left:1px solid #603811; line-height:8px; padding-left:10px;">' + add_notes + '</div>'

        add_notes = '<table width = "100%" border = "0" cellspacing = "0" cellpadding = "0" ' \
                    'style = "border-collapse: collapse; border: 1px solid #d1cdc7;"><tr><td align = "left" ' \
                    'style = "background-color: #eae7e9; border-left: 5px solid #d1cdc7; padding: 10px 10px 10px 10px;">' \
                    '<div style = "font-family: monospace; font-size: 40px; color: #d1cdc7; margin-bottom: -50px;">&ldquo;' \
                    '</div><div style = "font-family: monospace ; font-size: 14px; color: #252525; line-height: 18px; padding: 10px 10px 10px 40px;">' \
                    '<p><font color = "#808080"><i>Комментарий исполнителя:' + add_notes + '</i></font></strong></p></div>' \
                    '<div style = "font-family: monospace; font-size: 40px; color: #d1cdc7; line-height: 18px;">&rdquo;</div></td></tr></table>'

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">

<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">

<table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr align="top">
    <td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr>
    <td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
            <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
    </td>
    <td align="right" bgcolor="#f1eff0" width="400">
    <div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
        <b>Отдел расчетов</b>
    </div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr>
    <td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
    </tr>
    <tr>
    <td>&nbsp;</td>
    </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 10px 0px 10px 0px;">
<tr>
<td align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; line-height: 18px;">

<table cellspacing="0">
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;''' + ' <b>' + strParam +  '</b> изменился с <b>' + oldParam + '</b> на <b>' + newParam + '''</FONT></td>
   </tr>
</table>
<br />
<a href="https://helpdesk.teztour.com/issues/''' + issueID + '''"><strong> Задача #''' + issueID + ': ' + title + '''</strong></a><br />
<br />
<table cellspacing="0">
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Автор:</FONT></td><td><FONT size=2>''' + author + '''</FONT></td>
    </tr>
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=2>''' + status + '''</FONT></td>
   </tr>
   <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Приоритет:</FONT></td><td><FONT size=2>''' + priority + '''</FONT></td>
   </tr>
     <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Исполнитель:</FONT></td><td><FONT size=2>''' + assigned + '''</FONT></td>
   </tr>
     <tr>
    <td><FONT size=2>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=2>''' + dateCreated  + '''</FONT></td>
   </tr>
  </table>
<div style="line-height:18px;">
    <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color:#000000;line-height:20px;">
        <pre>''' + add_notes + body + ''' </pre>

    </span>
</div> <br />
'''
    return html

def template_html_Assigned (issueID, body, strParam, oldParam, newParam, dateCreated, title, author, status, priority, assigned, add_notes) :

    if add_notes != '':
        # add_notes = '<div style = "border-left:1px solid #603811; line-height:8px; padding-left:10px;">' + add_notes + '</div>'

        add_notes = '<table width = "100%" border = "0" cellspacing = "0" cellpadding = "0" ' \
                    'style = "border-collapse: collapse; border: 1px solid #d1cdc7;"><tr><td align = "left" ' \
                    'style = "background-color: #eae7e9; border-left: 5px solid #d1cdc7; padding: 10px 10px 10px 10px;">' \
                    '<div style = "font-family: monospace; font-size: 40px; color: #d1cdc7; margin-bottom: -50px;">&ldquo;' \
                    '</div><div style = "font-family: monospace ; font-size: 14px; color: #252525; line-height: 18px; padding: 10px 10px 10px 40px;">' \
                    '<p><font color = "#808080"><i>Комментарий исполнителя:' + add_notes + '</i></font></strong></p></div>' \
                    '<div style = "font-family: monospace; font-size: 40px; color: #d1cdc7; line-height: 18px;">&rdquo;</div></td></tr></table>'

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">

<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">

<table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">

<!-- Стильная шапка -->
<tr>
<td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; width:100%; margin:0; padding:0;">
	<tbody>
		<tr>
			<td style="padding: 25px 20px; text-align: left;">
				<div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); border-radius: 8px; padding: 15px; display: inline-block; border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
					<a href="http://www.tez-tour.com" target="_blank">
						<img alt="TEZ TOUR" src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" title="TEZ TOUR" style="max-height: 50px; filter: brightness(1.2) contrast(1.1);" />
					</a>
				</div>
			</td>
			<td style="padding: 25px 20px; text-align: right;">
				<div style="color:#ffffff; font-family:Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:18px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
					<strong>Служба технической поддержки TEZ TOUR</strong><br />
					Email: <a href="mailto:help@tez-tour.com" target="_blank" style="color: #ffffff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.5);">help@tez-tour.com</a>
				</div>
			</td>
		</tr>
	</tbody>
</table>
</td>
</tr>

<!-- Тонкая красная акцентная полоса -->
<tr>
<td style="padding: 0; margin: 0;">
<div style="width: 100%; height: 1px; background: linear-gradient(90deg, #e94560 0%, #ff6b6b 50%, #e94560 100%); margin: 0; padding: 0;"></div>
</td>
</tr>

<!-- Стильный основной контент -->
<tr>
<td style="padding: 30px 25px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-left: 4px solid #3498db;">
<div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #2c3e50; line-height: 1.6;">

<!-- Информация об изменении -->
<div style="background: rgba(52, 152, 219, 0.1); border-radius: 6px; padding: 15px; margin-bottom: 20px; border-left: 3px solid #3498db;">
<table cellspacing="0" style="width: 100%;">
   <tr>
    <td style="color: #2c3e50; font-weight: 500;">&nbsp;&nbsp;&bull;&nbsp;''' + ' <b>' + strParam +  '</b> изменился с <b>' + oldParam + '</b> на <b>' + newParam + '''</td>
   </tr>
</table>
</div>

<!-- Ссылка на задачу -->
<div style="margin-bottom: 20px;">
<a href="https://helpdesk.teztour.com/issues/''' + issueID + '''" style="color: #3498db; text-decoration: none; font-weight: 600; font-size: 16px; border-bottom: 2px solid #3498db; padding-bottom: 2px;"><strong>Задача #''' + issueID + ': ' + title + '''</strong></a>
</div>

<!-- Детали задачи -->
<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin-bottom: 25px; border: 1px solid #e9ecef;">
<table cellspacing="0" style="width: 100%;">
   <tr>
    <td style="color: #6c757d; font-weight: 500; padding: 5px 0;">&nbsp;&nbsp;&bull;&nbsp;Автор:</td><td style="color: #2c3e50; padding: 5px 0;">''' + author + '''</td>
   </tr>
   <tr>
    <td style="color: #6c757d; font-weight: 500; padding: 5px 0;">&nbsp;&nbsp;&bull;&nbsp;Статус:</td><td style="color: #2c3e50; padding: 5px 0;">''' + status + '''</td>
   </tr>
   <tr>
    <td style="color: #6c757d; font-weight: 500; padding: 5px 0;">&nbsp;&nbsp;&bull;&nbsp;Приоритет:</td><td style="color: #2c3e50; padding: 5px 0;">''' + priority + '''</td>
   </tr>
   <tr>
    <td style="color: #6c757d; font-weight: 500; padding: 5px 0;">&nbsp;&nbsp;&bull;&nbsp;Исполнитель:</td><td style="color: #2c3e50; padding: 5px 0;">''' + assigned + '''</td>
   </tr>
   <tr>
    <td style="color: #6c757d; font-weight: 500; padding: 5px 0;">&nbsp;&nbsp;&bull;&nbsp;Дата создания:</td><td style="color: #2c3e50; padding: 5px 0;">''' + dateCreated + '''</td>
   </tr>
</table>
</div>

<!-- Основной текст -->
<div style="background: #ffffff; border-radius: 8px; padding: 20px; border: 1px solid #e9ecef; margin-bottom: 25px;">
<span style="font-family: 'Segoe UI', Arial, Helvetica, sans-serif; font-size: 14px; color:#2c3e50; line-height:1.6;">
<pre style="font-family: 'Segoe UI', Arial, Helvetica, sans-serif; white-space: pre-wrap; margin: 0;">''' + add_notes + body + '''</pre>
</span>
</div>

<!-- Информационное сообщение -->
<div style="background: rgba(255, 193, 7, 0.1); border-radius: 8px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #ffc107;">
<p style="text-align: justify; margin: 0; color: #856404; font-size: 13px; line-height: 1.5;">
<em>
Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
<a href="mailto:help@tez-tour.com" target="_blank" style="color: #856404; text-decoration: underline;">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
</em>
</p>
</div>

<!-- Ссылка на портал -->
<div style="background: rgba(40, 167, 69, 0.1); border-radius: 8px; padding: 20px; border-left: 4px solid #28a745;">
<p style="margin: 0; color: #155724; font-size: 14px; line-height: 1.5;">
Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
<a href="https://its.tez-tour.com" style="color: #155724; text-decoration: underline; font-weight: 500;">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>
</div>

</div>
</td>
</tr>

<!-- Стильный футер -->
<tr>
<td style="padding: 0; margin: 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 0; padding: 0; width: 100%;">
<tr>
<td style="padding: 20px 25px; margin: 0;">
    <!-- Основная информация -->
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 15px;">
        <!-- Логотип и название -->
        <div style="display: flex; align-items: center; gap: 15px;">
            <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" style="max-height: 35px; width: auto; filter: brightness(1.2) contrast(1.1);" />
            <div style="font-family: 'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size: 16px; color: #ffffff; line-height: 1.5; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                <span style="font-weight: 600; color: #ffffff; font-size: 18px;">Международный туроператор <strong style="color: #3498db;">TEZ TOUR</strong></span><br>
                <a href="http://www.tez-tour.com" target="_blank" style="color: #3498db; text-decoration: none; font-weight: 500; transition: color 0.3s ease;">www.tez-tour.com</a>
            </div>
        </div>
    </div>

</td>
</tr>
</table>
</td>
</tr>

</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html



def template_html_AddNotes (issueID, notes) :
    html = '''
<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); border-collapse:collapse; border-radius:8px 8px 0 0; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:25px 20px; text-align:left">
			<div style="backdrop-filter:blur(10px); background:rgba(255, 255, 255, 0.15); border-radius:8px; border:1px solid rgba(255, 255, 255, 0.2); box-shadow:0 4px 15px rgba(0,0,0,0.2); display:inline-block; padding:15px"><a href="http://www.tez-tour.com" target="_blank"><img alt="TEZ TOUR" src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" style="filter:brightness(1.2) contrast(1.1); max-height:50px" title="TEZ TOUR" /> </a></div>
			</td>
			<td style="padding:25px 20px; text-align:right">
			<div style="color:#ffffff; font-family:Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:18px; text-shadow:0 2px 4px rgba(0,0,0,0.3)"><strong>Служба технической поддержки TEZ TOUR</strong><br />
			Email: <a href="mailto:help@tez-tour.com" style="color: #ffffff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.5);" target="_blank">help@tez-tour.com</a></div>
			</td>
		</tr>
	</tbody>
</table>
<!-- Тонкая красная акцентная полоса без разрывов -->

<div style="background:linear-gradient(90deg, #e94560 0%, #ff6b6b 50%, #e94560 100%); height:4px; margin-bottom:0px; margin-left:0px; margin-right:0px; margin-top:0px; padding:0; width:100%">&nbsp;</div>
<!-- Основной контент - без лишних отступов -->

<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #faf7f3 0%, #f8f6f2 100%); border-collapse:collapse; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:25px 25px 30px 25px; text-align:left">
			<!-- Стилизованный блок с комментарием -->
			<div style="background:linear-gradient(135deg, #ecf0f1 0%, #e8f4f8 100%); border-radius:10px; border:1px solid #d5dbdb; box-shadow:0 4px 15px rgba(0,0,0,0.1); padding:25px; margin-bottom:20px;">
				<div style="border-left:4px solid #3498db; padding-left:20px;">
					<h3 style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:18px; font-weight:600; margin-bottom:15px; margin-left:15px; margin-right:15px; margin-top:15px; text-shadow:0 1px 2px rgba(0,0,0,0.1); text-align:left">Новый комментарий</h3>

					<div style="background:rgba(255,255,255,0.8); border-radius:6px; box-shadow:inset 0 1px 3px rgba(0,0,0,0.1); color:#34495e; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:15px; line-height:1.6; padding:20px; text-align:left; word-wrap:break-word; white-space:pre-wrap;">
						<p style="margin-bottom:15px; color:#2c3e50; font-weight:500;">В задачу <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''" style="color:#3498db; text-decoration:none; border-bottom:1px solid #3498db;"><strong>#''' + issueID + '''</strong></a> добавлен новый комментарий:</p>

						<div style="background:rgba(52, 152, 219, 0.1); border-left:3px solid #3498db; border-radius:6px; padding:15px; margin-top:15px;">
							<pre style="font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:14px; color:#34495e; line-height:1.6; margin:0; white-space:pre-wrap; word-wrap:break-word;">''' + notes + '''</pre>
						</div>
					</div>
				</div>
			</div>
			</td>
		</tr>
	</tbody>
</table>
<!-- Футер -->

<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #2c3e50 0%, #34495e 100%); border-collapse:collapse; border-radius:0 0 8px 8px; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:20px 25px; margin:0;">
				<!-- Основная информация -->
				<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:15px;">
					<!-- Логотип и название -->
					<div style="display:flex; align-items:center; gap:15px;">
						<img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" style="max-height:35px; width:auto; filter:brightness(1.2) contrast(1.1);" />
						<div style="font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:16px; color:#ffffff; line-height:1.5; text-shadow:0 2px 4px rgba(0,0,0,0.3);">
							<span style="font-weight:600; color:#ffffff; font-size:18px;">Международный туроператор <strong style="color:#3498db;">TEZ TOUR</strong></span><br>
							<a href="http://www.tez-tour.com" target="_blank" style="color:#3498db; text-decoration:none; font-weight:500; transition:color 0.3s ease;">www.tez-tour.com</a>
						</div>
					</div>
				</div>

			</td>
		</tr>
	</tbody>
</table>
'''
    return html

def template_html_AddNotes_Ufa (issueID, notes) :
    html = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">

<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">

<table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr align="top">
    <td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr>
    <td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
    </td>
    <td align="right" bgcolor="#f1eff0" width="400">
    <div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
        <b>Отдел расчетов</b>
    </div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
    <tr>
    <td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
    </tr>
    <tr>
    <td>&nbsp;</td>
    </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; margin: 10px 0px 10px 0px;">
<tr>
<td align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; line-height: 18px;">
<p>В задачу <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''"> <strong>#''' + issueID + '''</strong></a> добавлен новый комментарий: </p>
<div style="line-height:18px;">
    <span style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color:#000000;line-height:16px">
        <pre>''' + notes + ''' </pre>
    </span>
</div>
'''
    return html

def template_html_new_issue_content (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Контент-Центр TEZ TOUR</b><br><a href="tel:+7(495) 775-10-09">+7(495) 775-10-09</a>, <a href="tel:+7(495) 660-10-09"> +7(495) 660-10-09</a>, вн.1435<br>Email: <a href="mailto:content@tez-tour.com" target="_blank">content@tez-tour.com</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/><br/>
Ваше обращение в Контент-Центр зарегистрировано в системе под номером - #<strong>''' + issueID + '''</strong><br />
Сохраняйте, пожалуйста, историю переписки.<br />
<p style="text-align: justify;">
    <ins>
        <small>
            <em>
                Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                <a href="mailto:content@tez-tour.com" target="_blank">content@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
            </em>
        </small>
    </ins>
</p>
<p>
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html_new_issue_egypt (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Technical support team TEZ TOUR Egypt</b><br>Email: <a href="mailto:help.eg@tez-tour.com" target="_blank">help.eg@tez-tour.com</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Hello!<br/><br/>
Your message to the Development Department registered in the system under - #<strong>''' + issueID + '''</strong><br />
Save please e-mails history.<br />
<p align=justify><ins><small><em>Please wait for our reply and don’t create new requests by sending email to <a href="mailto:help.eg@tez-tour.com" target="_blank">help.eg@tez-tour.com</a>.
It will only increase the processing time of your mail. Please when replying don’t change the email subject.</em></ins></small></p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Subject:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Status:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Date of creation:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
International Tour Operator <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html_new_issue_msk_watcher(issueID, subject, description, status, created_on) :

    html= '''
<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); border-collapse:collapse; border-radius:8px 8px 0 0; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:15px 15px; text-align:left">
			<div style="backdrop-filter:blur(10px); background:rgba(255, 255, 255, 0.15); border-radius:8px; border:1px solid rgba(255, 255, 255, 0.2); box-shadow:0 4px 15px rgba(0,0,0,0.2); display:inline-block; padding:12px"><a href="http://www.tez-tour.com" target="_blank"><img alt="TEZ TOUR" src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" style="filter:brightness(1.2) contrast(1.1); max-height:45px" title="TEZ TOUR" /> </a></div>
			</td>
			<td style="padding:15px 15px; text-align:right">
			<div style="color:#ffffff; font-family:Tahoma,Verdana,Arial,sans-serif; font-size:13px; line-height:16px; text-shadow:0 2px 4px rgba(0,0,0,0.3)"><strong>Служба технической поддержки TEZ TOUR</strong><br />
			Email: <a href="mailto:help@tez-tour.com" style="color: #ffffff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.5);" target="_blank">help@tez-tour.com</a></div>
			</td>
		</tr>
	</tbody>
</table>
<!-- Тонкая красная акцентная полоса без разрывов -->

<div style="background:linear-gradient(90deg, #e94560 0%, #ff6b6b 50%, #e94560 100%); height:3px; margin-bottom:0px; margin-left:0px; margin-right:0px; margin-top:0px; padding:0; width:100%">&nbsp;</div>
<!-- Основной контент - без лишних отступов -->

<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #faf7f3 0%, #f8f6f2 100%); border-collapse:collapse; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:15px 15px 20px 15px"><!-- Приветствие -->
			<div style="margin-bottom:15px">
			<h2 style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:18px; font-weight:600; margin-bottom:10px; margin-left:10px; margin-right:10px; margin-top:10px; text-shadow:0 1px 2px rgba(0,0,0,0.1)">Здравствуйте!</h2>
			</div>
			<!-- Детали задачи -->

			<div style="background:linear-gradient(135deg, #ecf0f1 0%, #e8f4f8 100%); border-radius:8px; border:1px solid #d5dbdb; box-shadow:0 4px 15px rgba(0,0,0,0.1); padding:15px; margin-bottom:15px">
			<div style="border-left:4px solid #3498db; padding-left:15px">
			<h3 style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:16px; font-weight:600; margin-bottom:10px; margin-left:10px; margin-right:10px; margin-top:10px; text-shadow:0 1px 2px rgba(0,0,0,0.1)">Детали задачи</h3>

			<div style="background:rgba(255,255,255,0.8); border-radius:6px; box-shadow:inset 0 1px 3px rgba(0,0,0,0.1); color:#34495e; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:1.5; padding:15px">
				<table cellspacing="0" style="width:100%">
					<tr>
						<td style="padding:6px 0; color:#6c757d; font-weight:500;">Тема:</td>
						<td style="padding:6px 0; color:#2c3e50; font-weight:600;">''' + subject + '''</td>
					</tr>
					<tr>
						<td style="padding:6px 0; color:#6c757d; font-weight:500;">Статус:</td>
						<td style="padding:6px 0; color:#2c3e50; font-weight:600;">''' + status + '''</td>
					</tr>
					<tr>
						<td style="padding:6px 0; color:#6c757d; font-weight:500;">Дата создания:</td>
						<td style="padding:6px 0; color:#2c3e50; font-weight:600;">''' + created_on + '''</td>
					</tr>
				</table>
			</div>
			</div>
			</div>
			<!-- Описание задачи -->

			<div style="background:linear-gradient(135deg, #ecf0f1 0%, #e8f4f8 100%); border-radius:8px; border:1px solid #d5dbdb; box-shadow:0 4px 15px rgba(0,0,0,0.1); padding:15px; margin-bottom:15px">
			<div style="border-left:4px solid #f39c12; padding-left:15px">
			<h3 style="color:#2c3e50; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:16px; font-weight:600; margin-bottom:10px; margin-left:10px; margin-right:10px; margin-top:10px; text-shadow:0 1px 2px rgba(0,0,0,0.1)">Описание</h3>

			<div style="background:rgba(255,255,255,0.8); border-radius:6px; box-shadow:inset 0 1px 3px rgba(0,0,0,0.1); color:#34495e; font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:14px; line-height:1.5; padding:15px">
				<pre style="font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; white-space:pre-wrap; margin:0; color:#34495e;">''' + description + '''</pre>
			</div>
			</div>
			</div>
			<!-- Информационные блоки -->

			<div style="background:rgba(255, 193, 7, 0.1); border-radius:6px; padding:15px; margin-bottom:15px; border-left:4px solid #ffc107">
			<p style="text-align:justify; margin:0; color:#856404; font-size:12px; line-height:1.4">
				<em>
					Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
					<a href="mailto:help@tez-tour.com" target="_blank" style="color:#856404; text-decoration:underline;">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
				</em>
			</p>
			</div>

			<div style="background:rgba(40, 167, 69, 0.1); border-radius:6px; padding:15px; border-left:4px solid #28a745">
			<p style="margin:0; color:#155724; font-size:13px; line-height:1.4">
				Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
				<a href="https://its.tez-tour.com" style="color:#155724; text-decoration:underline; font-weight:500;">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
			</p>
			</div>
			</td>
		</tr>
	</tbody>
</table>
<!-- Футер -->

<table border="0" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #2c3e50 0%, #34495e 100%); border-collapse:collapse; border-radius:0 0 8px 8px; margin:0; padding:0; width:100%">
	<tbody>
		<tr>
			<td style="padding:15px 15px; margin:0;">
				<!-- Основная информация -->
				<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:10px;">
					<!-- Логотип и название -->
					<div style="display:flex; align-items:center; gap:12px;">
						<img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" style="max-height:30px; width:auto; filter:brightness(1.2) contrast(1.1);" />
						<div style="font-family:'Segoe UI',Tahoma,Verdana,Arial,sans-serif; font-size:14px; color:#ffffff; line-height:1.4; text-shadow:0 2px 4px rgba(0,0,0,0.3);">
							<span style="font-weight:600; color:#ffffff; font-size:16px;">Международный туроператор <strong style="color:#3498db;">TEZ TOUR</strong></span><br>
							<a href="http://www.tez-tour.com" target="_blank" style="color:#3498db; text-decoration:none; font-weight:500; transition:color 0.3s ease;">www.tez-tour.com</a>
						</div>
					</div>
				</div>
			</td>
		</tr>
	</tbody>
</table>
'''
    return html

def template_html_new_issue_ukr_watcher(issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Служба технической поддержки Тез Тур Украина</b><br><a href="tel:+ 380 (44) 495-55-05">+ 380 (44) 495-55-05</a>, вн.4156/4148/4170<br>Email: <a href="mailto: it@teztour.com.ua" target="_blank">it@teztour.com.ua</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/><br/>
Вы получили данное Уведомление т.к. являетесь "Наблюдателем" по задаче или (и) ваш почтовый адрес указан в копии данного обращения - <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''"><strong>#''' + issueID + '''</strong></a><br/>
Сохраняйте, пожалуйста, историю переписки.<br />
<p style="text-align: justify;">
    <ins>
        <small>
            <em>
                Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                <a href="mailto:help@tez-tour.com" target="_blank">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
            </em>
        </small>
    </ins>
</p>
<p>
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html

def template_html_new_issue_content_Minsk (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Контент-Центр TEZ TOUR MINSK</b><br>Email: <a href="mailto:content@minsk.tez-tour.com" target="_blank">content@minsk.tez-tour.com</a>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/><br/>
Ваше обращение в Контент-Центр зарегистрировано в системе под номером - #<strong>''' + issueID + '''</strong><br />
Сохраняйте, пожалуйста, историю переписки.<br />
<p style="text-align: justify;">
    <ins>
        <small>
            <em>
                Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                <a href="mailto:content@minsk.tez-tour.com" target="_blank">content@minsk.tez-tour.com</a>, так как это может увеличить время обработки вашего запроса.<br>
                При ответах, пожалуйста, не изменяйте тему письма.
            </em>
        </small>
    </ins>
</p>
<p>
    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
</p>

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html



def template_html_new_issue_Ufa (issueID, subject, description, status, created_on) :

    html= '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;"><table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="top">
<td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
        <a href="http://www.tez-tour.com" target="_blank"><img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"></a>
</td>
<td align="right" bgcolor="#f1eff0" width="400">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
<b>Отдел расчетов</b>
</div>
</td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
Здравствуйте!<br/>
Ваше письмо получено и находится в работе. Пожалуйста, дождитесь ответа.<br />

<table cellspacing="0">
   <tr>
  <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Тема:</FONT></td><td><FONT size=3><strong>''' + subject + '''</FONT></strong></td>
    </tr>
   <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Статус:</FONT></td><td><FONT size=3><strong>''' + status + '''</FONT></strong></strong></td>
   </tr>
     <tr>
    <td><FONT size=3>&nbsp;&nbsp;&bull;&nbsp;Дата создания:</FONT></td><td><FONT size=3><strong>''' + created_on  + '''</FONT></strong></td>
   </tr>
</table>
<br />
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;"></td>
</tr>
<tr>
<td>&nbsp; <pre>''' + description + ''' </pre></td>
</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
</tr>
<tr>
<td bgcolor="#f1eff0">&nbsp;</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr>
<td width="280" align="left" bgcolor="#f1eff0">
<div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
Международный туроператор <b>TEZ TOUR</b><br>
<a href="http://www.tez-tour.com" target="_blank">www.tez-tour.com</a>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html


def template_html_new_issue_vln(issueID, subject, description, status, created_on):
    # Экранируем специальные символы для безопасности
    safe_subject = escape(subject)
    safe_status = escape(status)
    safe_created_on = escape(created_on)

    html_template = '''
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body style="margin:0px; padding: 0px; width: 100%; height: 100%;">
    <table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
        <tr>
            <td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">
                <table width="700" border="1" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                    <tr align="top">
                        <td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                <tr>
                                    <td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
                                        <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png"
                                             alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0">
                                    </td>
                                    <td align="right" bgcolor="#f1eff0" width="400">
                                        <div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
                                            <b>Служба технической поддержки TEZ TOUR</b><br><br>
                                            Email: <a href="mailto:help@tez-tour.com" target="_blank">help@tez-tour.com</a>
                                        </div>
                                    </td>
                                </tr>
                            </table>

                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                <tr>
                                    <td style="border-bottom: 1px solid #d1cdc7;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                </tr>
                            </table>

                            Здравствуйте!<br/><br/>
                            Ваше обращение в IT-Департамент зарегистрировано в системе под номером - #<strong>''' + issueID + '''</strong><br />
                            Сохраняйте, пожалуйста, историю переписки.<br />
                            <p style="text-align: justify;">
                                <ins>
                                    <small>
                                        <em>
                                            Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                                            <a href="mailto:help@tez-tour.com" target="_blank">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса.
                                            При ответах, пожалуйста, не изменяйте тему письма.
                                        </em>
                                    </small>
                                </ins>
                            </p>
                            <p>
                                Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
                                <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
                            </p>

                            <table cellspacing="0">
                                <tr>
                                    <td><font size="3">&nbsp;&nbsp;&bull;&nbsp;Тема:</font></td>
                                    <td><font size="3"><strong>''' + safe_subject + '''</strong></font></td>
                                </tr>
                                <tr>
                                    <td><font size="3">&nbsp;&nbsp;&bull;&nbsp;Статус:</font></td>
                                    <td><font size="3"><strong>''' + safe_status + '''</strong></font></td>
                                </tr>
                                <tr>
                                    <td><font size="3">&nbsp;&nbsp;&bull;&nbsp;Дата создания:</font></td>
                                    <td><font size="3"><strong>''' + safe_created_on + '''</strong></font></td>
                                </tr>
                            </table>
                            <br />

                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                <tr>
                                    <td style="border-bottom: 1px solid #d1cdc7;"></td>
                                </tr>
                                <tr>
                                    <td>&nbsp; <pre>''' + description + ''' </pre></td>
                                </tr>
                            </table>

                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                <tr>
                                    <td style="border-bottom: 1px solid #d1cdc7;" bgcolor="#f1eff0">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td bgcolor="#f1eff0">&nbsp;</td>
                                </tr>
                            </table>

                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
                                <tr>
                                    <td width="280" align="left" bgcolor="#f1eff0">
                                        <div style="font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 11px; color: #252525;">
                                            Международный туроператор <b>TEZ TOUR</b><br>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
'''
    return html_template


def template_html_new(issueID, body, strParam, oldParam, newParam, dateCreated, author, status, priority, assigned):
    html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Обновление задачи TEZ TOUR</title>
    <!--[if mso]>
    <noscript>
        <xml>
            <o:OfficeDocumentSettings>
                <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
    </noscript>
    <![endif]-->
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f4; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333333;">
    <!-- Email Container -->
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td align="center" style="padding: 20px 0;">
                <!-- Main Content Table -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); overflow: hidden;">

                    <!-- Header Section -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #ecd8bf 0%, #d4c4a8 100%); padding: 30px 40px;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td>
                                        <a href="http://www.tez-tour.com" target="_blank" style="text-decoration: none;">
                                            <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png"
                                                 alt="TEZ TOUR"
                                                 style="width: 180px; height: auto; display: block;"
                                                 width="180">
                                        </a>
                                    </td>
                                    <td align="right" style="vertical-align: top;">
                                        <div style="font-size: 14px; color: #2c2c2c; line-height: 1.4;">
                                            <strong style="color: #1a1a1a; font-size: 16px;">Служба технической поддержки</strong><br>
                                            <span style="font-size: 13px;">
                                               <a href="mailto:help@tez-tour.com" style="color: #2c2c2c; text-decoration: none;">help@tez-tour.com</a>
                                            </span>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Main Content Section -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px;">
                            <!-- Task Update Notification -->
                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 8px; margin-bottom: 25px; color: white;">
                                <h2 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 600;">
                                    <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''" style="color: white; text-decoration: none;">Задача #''' + issueID + '''</a> была обновлена
                                </h2>
                                <p style="margin: 0; font-size: 14px; opacity: 0.9;">
                                    ''' + strParam + ''' изменился с <strong>''' + oldParam + '''</strong> на <strong>''' + newParam + '''</strong>
                                </p>
                            </div>

                            <!-- Task Details Section -->
                            <div style="background-color: #f8f9fa; border-radius: 8px; padding: 25px; margin-bottom: 25px;">
                                <h3 style="margin: 0 0 20px 0; font-size: 18px; color: #2c2c2c; font-weight: 600;">Детали задачи</h3>

                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                    <tr>
                                        <td style="padding: 8px 0; border-bottom: 1px solid #e9ecef;">
                                            <span style="font-size: 14px; color: #6c757d; font-weight: 500;">Автор:</span>
                                            <span style="font-size: 14px; color: #2c2c2c; font-weight: 600; margin-left: 10px;">''' + author + '''</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 8px 0; border-bottom: 1px solid #e9ecef;">
                                            <span style="font-size: 14px; color: #6c757d; font-weight: 500;">Статус:</span>
                                            <span style="font-size: 14px; color: #2c2c2c; font-weight: 600; margin-left: 10px;">''' + status + '''</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 8px 0; border-bottom: 1px solid #e9ecef;">
                                            <span style="font-size: 14px; color: #6c757d; font-weight: 500;">Приоритет:</span>
                                            <span style="font-size: 14px; color: #2c2c2c; font-weight: 600; margin-left: 10px;">''' + priority + '''</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 8px 0; border-bottom: 1px solid #e9ecef;">
                                            <span style="font-size: 14px; color: #6c757d; font-weight: 500;">Исполнитель:</span>
                                            <span style="font-size: 14px; color: #2c2c2c; font-weight: 600; margin-left: 10px;">''' + assigned + '''</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 8px 0;">
                                            <span style="font-size: 14px; color: #6c757d; font-weight: 500;">Дата создания:</span>
                                            <span style="font-size: 14px; color: #2c2c2c; font-weight: 600; margin-left: 10px;">''' + dateCreated + '''</span>
                                        </td>
                                    </tr>
                                </table>
                            </div>

                            <!-- Description Section -->
                            <div style="background-color: #ffffff; border: 1px solid #dee2e6; border-radius: 6px; padding: 20px; margin-bottom: 25px;">
                                <h3 style="margin: 0 0 15px 0; font-size: 16px; color: #2c2c2c; font-weight: 600;">Описание</h3>
                                <div style="font-size: 14px; color: #333333; line-height: 1.6; white-space: pre-wrap; word-wrap: break-word;">
                                    ''' + body + '''
                                </div>
                            </div>
                        </td>
                    </tr>

                    <!-- Auto Message Warning -->
                    <tr>
                        <td style="padding: 0 40px;">
                            <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px 20px; border-radius: 4px; margin-bottom: 25px;">
                                <p style="margin: 0; font-size: 13px; color: #856404; font-style: italic; line-height: 1.5;">
                                    <strong>Это автоматическое сообщение.</strong> Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                                    <a href="mailto:help@tez-tour.com" style="color: #856404; text-decoration: underline;">help@tez-tour.com</a>,
                                    так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
                                </p>
                            </div>
                        </td>
                    </tr>

                    <!-- Enhanced Portal Link Section with Redmine Features -->
                    <tr>
                        <td style="padding: 0 40px 25px 40px;">
                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 25px; margin-bottom: 25px; box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3); position: relative; overflow: hidden;">

                                <!-- Decorative elements -->
                                <div style="position: absolute; top: -20px; right: -20px; width: 80px; height: 80px; background: rgba(255, 255, 255, 0.1); border-radius: 50%;"></div>
                                <div style="position: absolute; bottom: -30px; left: -30px; width: 100px; height: 100px; background: rgba(255, 255, 255, 0.05); border-radius: 50%;"></div>

                                <!-- Header -->
                                <div style="position: relative; z-index: 2;">
                                    <h3 style="margin: 0 0 15px 0; font-size: 20px; color: #ffffff; font-weight: 700;">
                                        Удобный способ работы с задачами в Redmine
                                    </h3>

                                    <!-- Main content -->
                                    <div style="color: #ffffff; line-height: 1.6; margin-bottom: 20px;">
                                        <p style="margin: 0 0 12px 0; font-size: 15px; font-weight: 500;">
                                            <strong>Полный контроль над вашими задачами:</strong>
                                        </p>

                                        <!-- Features list -->
                                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 15px 0;">
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                Kanban доска с drag & drop
                                            </div>
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                Реальное время обновлений
                                            </div>
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                14 статусов с анимацией
                                            </div>
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                Push-уведомления
                                            </div>
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                Статистика и аналитика
                                            </div>
                                            <div style="display: flex; align-items: center; font-size: 13px;">
                                                <span style="color: #4ade80; margin-right: 8px; font-size: 14px;">✓</span>
                                                Мобильная адаптация
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Call to action -->
                                    <div style="background: rgba(255, 255, 255, 0.15); border-radius: 8px; padding: 15px; margin: 15px 0; border-left: 4px solid #4ade80;">
                                        <p style="margin: 0 0 10px 0; font-size: 14px; color: #ffffff; font-weight: 600;">
                                            Ускорьте работу с задачами в 3 раза!
                                        </p>
                                        <p style="margin: 0; font-size: 13px; color: rgba(255, 255, 255, 0.9);">
                                            Зарегистрируйтесь на <a href="https://its.tez-tour.com" style="color: #ffffff; text-decoration: none; font-weight: 600; border-bottom: 1px solid rgba(255, 255, 255, 0.5);">https://its.tez-tour.com</a>
                                            используя ваш аккаунт TEZ ERP для мгновенного доступа ко всем возможностям.
                                        </p>
                                    </div>

                                    <!-- Additional benefits -->
                                    <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(255, 255, 255, 0.2);">
                                        <div style="display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: rgba(255, 255, 255, 0.8);">
                                            <span>Мгновенные уведомления о статусах</span>
                                            <span>Работает на всех устройствах</span>
                                         </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>

                    <!-- Footer Section -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 30px 40px;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td style="vertical-align: top;">
                                        <div style="font-size: 12px; color: #6c757d; line-height: 1.4;">
                                            <strong style="color: #2c2c2c; font-size: 14px;">Международный туроператор TEZ TOUR</strong><br>
                                            <a href="http://www.tez-tour.com" target="_blank" style="color: #007bff; text-decoration: none;">www.tez-tour.com</a>
                                        </div>
                                    </td>

                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
'''
    return html



def template_html_new_issue_msk_new_template(issueID, subject, description, status, created_on):
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Новая заявка TEZ TOUR</title>
        <style>
            body { margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5; }
            .container { max-width: 600px; margin: 0 auto; background-color: #ffffff; }
            .header { background: linear-gradient(135deg, #ecd8bf 0%, #d4c4a8 100%); padding: 30px 20px; text-align: center; }
            .header h1 { color: #2c2c2c; margin: 0; font-size: 24px; font-weight: 600; }
            .content { padding: 30px 20px; }
            .greeting { color: #2c2c2c; font-size: 16px; margin-bottom: 25px; line-height: 1.6; }
            .issue-card { background: #f8f9fa; border-radius: 12px; padding: 25px; margin: 20px 0; border-left: 4px solid #ecd8bf; }
            .issue-header { display: flex; align-items: center; margin-bottom: 15px; }
            .issue-icon { background: #ecd8bf; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 15px; }
            .issue-title { font-size: 18px; color: #2c2c2c; font-weight: 600; }
            .issue-details { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px; }
            .detail-item { background: #ffffff; padding: 12px; border-radius: 8px; border: 1px solid #e9ecef; }
            .detail-label { color: #6c757d; font-size: 12px; text-transform: uppercase; font-weight: 600; margin-bottom: 5px; }
            .detail-value { color: #2c2c2c; font-size: 14px; font-weight: 500; }
            .status-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; }
            .status-new { background: #e3f2fd; color: #1976d2; }
            .status-in-progress { background: #fff3e0; color: #f57c00; }
            .status-resolved { background: #e8f5e8; color: #388e3c; }
            .description { background: #ffffff; border-radius: 8px; padding: 20px; margin: 20px 0; border: 1px solid #e9ecef; }
            .description h3 { color: #2c2c2c; margin: 0 0 15px 0; font-size: 16px; font-weight: 600; }
            .description p { color: #495057; line-height: 1.6; margin: 0; }
            .portal-section { background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; padding: 25px; margin: 25px 0; text-align: center; }
            .portal-title { color: #2c2c2c; font-size: 18px; font-weight: 600; margin-bottom: 15px; }
            .portal-features { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin: 20px 0; }
            .feature-item { background: #ffffff; padding: 10px 15px; border-radius: 8px; font-size: 12px; color: #495057; border: 1px solid #dee2e6; }
            .portal-link { display: inline-block; background: linear-gradient(135deg, #ecd8bf 0%, #d4c4a8 100%); color: #2c2c2c; text-decoration: none; padding: 12px 25px; border-radius: 8px; font-weight: 600; margin-top: 15px; transition: all 0.3s ease; }
            .portal-link:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
            .footer { background: #2c2c2c; color: #ffffff; text-align: center; padding: 20px; font-size: 12px; }
            .warning { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 15px; margin: 20px 0; color: #856404; }
            .warning strong { display: block; margin-bottom: 5px; }
            @media (max-width: 600px) {
                .issue-details { grid-template-columns: 1fr; }
                .portal-features { flex-direction: column; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>TEZ TOUR - Техническая поддержка</h1>
            </div>

            <div class="content">
                <div class="greeting">
                    Здравствуйте!<br>
                    Создана новая заявка в системе технической поддержки TEZ TOUR.
                </div>

                <div class="issue-card">
                    <div class="issue-header">
                        <div class="issue-icon">
                            <span style="font-size: 18px; color: #2c2c2c;">[Заявка]</span>
                        </div>
                        <div class="issue-title">Заявка #''' + issueID + '''</div>
                    </div>

                    <div class="issue-details">
                        <div class="detail-item">
                            <div class="detail-label">Тема</div>
                            <div class="detail-value">''' + subject + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Статус</div>
                            <div class="detail-value">
                                <span class="status-badge status-''' + status.lower().replace(' ', '-') + '''">''' + status + '''</span>
                            </div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Дата создания</div>
                            <div class="detail-value">''' + created_on + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Описание</div>
                            <div class="detail-value">''' + description + '''</div>
                        </div>
                    </div>
                </div>

                <div class="warning">
                    <strong>Важно:</strong>
                    Это автоматическое сообщение. Пожалуйста, не отвечайте на это письмо.
                </div>

                <div class="portal-section">
                    <div class="portal-title">Управляйте заявками в Redmine</div>
                    <p style="color: #495057; margin-bottom: 20px;">
                        Получите полный контроль над своими задачами с современной системой управления проектами
                    </p>

                    <div class="portal-features">
                        <div class="feature-item">Kanban доска</div>
                        <div class="feature-item">14 статусов</div>
                        <div class="feature-item">Push уведомления</div>
                        <div class="feature-item">Аналитика</div>
                        <div class="feature-item">Мобильная версия</div>
                        <div class="feature-item">Real-time обновления</div>
                    </div>

                    <a href="https://its.tez-tour.com" class="portal-link">
                        Открыть Redmine
                    </a>

                    <p style="font-size: 12px; color: #6c757d; margin-top: 15px;">
                        Используйте ваш аккаунт TEZ ERP для входа
                    </p>
                </div>
            </div>

            <div class="footer">
                <p>© 2026 TEZ TOUR. Все права защищены.</p>
                <p>Это автоматическое сообщение системы технической поддержки.</p>
            </div>
        </div>
    </body>
    </html>
    '''



def template_html_Assigned_new(issueID, body, strParam, oldParam, newParam, dateCreated, title, author, status, priority, assigned, add_notes):
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Обновление задачи TEZ TOUR</title>
        <style>
            body { margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif; background-color: #f5f5f5; }
            .container { max-width: 600px; margin: 0 auto; background-color: #ffffff; }
            .header { background: linear-gradient(135deg, #ecd8bf 0%, #d4c4a8 100%); padding: 25px 20px; }
            .header-content { display: flex; justify-content: space-between; align-items: center; }
            .logo { width: 180px; height: auto; }
            .contact-info { text-align: right; color: #2c2c2c; font-size: 12px; line-height: 1.4; }
            .contact-info a { color: #2c2c2c; text-decoration: none; }
            .content { padding: 30px 20px; }
            .greeting { color: #2c2c2c; font-size: 16px; margin-bottom: 25px; line-height: 1.6; }
            .issue-card { background: #f8f9fa; border-radius: 12px; padding: 25px; margin: 20px 0; border-left: 4px solid #ecd8bf; }
            .issue-header { display: flex; align-items: center; margin-bottom: 20px; }
            .issue-icon { background: #ecd8bf; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 15px; }
            .issue-title { font-size: 18px; color: #2c2c2c; font-weight: 600; }
            .issue-title a { color: #2c2c2c; text-decoration: none; }
            .issue-title a:hover { text-decoration: underline; }
            .change-highlight { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 15px; margin: 15px 0; }
            .change-text { color: #856404; font-size: 14px; margin: 0; }
            .issue-details { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px; }
            .detail-item { background: #ffffff; padding: 12px; border-radius: 8px; border: 1px solid #e9ecef; }
            .detail-label { color: #6c757d; font-size: 12px; text-transform: uppercase; font-weight: 600; margin-bottom: 5px; }
            .detail-value { color: #2c2c2c; font-size: 14px; font-weight: 500; }
            .status-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; }
            .status-new { background: #e3f2fd; color: #1976d2; }
            .status-in-progress { background: #fff3e0; color: #f57c00; }
            .status-resolved { background: #e8f5e8; color: #388e3c; }
            .status-closed { background: #f3e5f5; color: #7b1fa2; }
            .description { background: #ffffff; border-radius: 8px; padding: 20px; margin: 20px 0; border: 1px solid #e9ecef; }
            .description h3 { color: #2c2c2c; margin: 0 0 15px 0; font-size: 16px; font-weight: 600; }
            .description p { color: #495057; line-height: 1.6; margin: 0; }
            .notes-section { background: #f8f9fa; border-left: 4px solid #ecd8bf; border-radius: 8px; padding: 20px; margin: 20px 0; }
            .notes-header { color: #6c757d; font-size: 12px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px; }
            .notes-content { color: #495057; font-style: italic; line-height: 1.6; }
            .portal-section { background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; padding: 25px; margin: 25px 0; text-align: center; }
            .portal-title { color: #2c2c2c; font-size: 18px; font-weight: 600; margin-bottom: 15px; }
            .portal-subtitle { color: #495057; font-size: 14px; margin-bottom: 20px; line-height: 1.5; }
            .portal-features { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin: 20px 0; }
            .feature-item { background: #ffffff; padding: 8px 12px; border-radius: 6px; font-size: 11px; color: #495057; border: 1px solid #dee2e6; }
            .portal-link { display: inline-block; background: linear-gradient(135deg, #ecd8bf 0%, #d4c4a8 100%); color: #2c2c2c; text-decoration: none; padding: 12px 25px; border-radius: 8px; font-weight: 600; margin-top: 15px; transition: all 0.3s ease; }
            .portal-link:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
            .footer { background: #2c2c2c; color: #ffffff; text-align: center; padding: 20px; font-size: 12px; }
            .warning { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 15px; margin: 20px 0; color: #856404; }
            .warning strong { display: block; margin-bottom: 5px; }
            @media (max-width: 600px) {
                .header-content { flex-direction: column; text-align: center; }
                .contact-info { text-align: center; margin-top: 15px; }
                .issue-details { grid-template-columns: 1fr; }
                .portal-features { flex-direction: column; }
                .container { margin: 0; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="header-content">
                    <div>
                        <a href="http://www.tez-tour.com" target="_blank">
                            <img src="https://r.tez-tour.com/armmanager/images/teztour_logo.png" alt="TEZ TOUR" class="logo">
                        </a>
                    </div>
                    <div class="contact-info">
                        <strong>Служба технической поддержки TEZ TOUR</strong><br>
                        Email: <a href="mailto:help@tez-tour.com">help@tez-tour.com</a>
                    </div>
                </div>
            </div>

            <div class="content">
                <div class="greeting">
                    Здравствуйте!<br>
                    Задача была обновлена в системе технической поддержки TEZ TOUR.
                </div>

                <div class="issue-card">
                    <div class="issue-header">
                        <div class="issue-icon">
                            <span style="font-size: 18px; color: #2c2c2c;"></span>
                        </div>
                        <div class="issue-title">
                            <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''">Задача #''' + issueID + '''</a>
                        </div>
                    </div>

                    <div class="change-highlight">
                        <p class="change-text">
                            <strong>''' + strParam + '''</strong> изменился с <strong>''' + oldParam + '''</strong> на <strong>''' + newParam + '''</strong>
                        </p>
                    </div>

                    <div class="issue-details">
                        <div class="detail-item">
                            <div class="detail-label">Название</div>
                            <div class="detail-value">''' + title + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Автор</div>
                            <div class="detail-value">''' + author + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Статус</div>
                            <div class="detail-value">
                                <span class="status-badge status-''' + status.lower().replace(' ', '-') + '''">''' + status + '''</span>
                            </div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Приоритет</div>
                            <div class="detail-value">''' + priority + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Исполнитель</div>
                            <div class="detail-value">''' + assigned + '''</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Дата создания</div>
                            <div class="detail-value">''' + dateCreated + '''</div>
                        </div>
                    </div>
                </div>

                <div class="description">
                    <h3>Описание задачи</h3>
                    <p>''' + body + '''</p>
                </div>

                ''' + ('''
                <div class="notes-section">
                    <div class="notes-header">Комментарий исполнителя</div>
                    <div class="notes-content">''' + add_notes + '''</div>
                </div>
                ''' if add_notes else '') + '''

                <div class="warning">
                    <strong>Важно:</strong>
                    Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на <a href="mailto:help@tez-tour.com">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
                </div>

                <div class="portal-section">
                    <div class="portal-title">Управляйте задачами в TEZ Navigator</div>
                    <div class="portal-subtitle">
Получите полный контроль над своими задачами с помощью современной системы управления задачами. Отслеживайте прогресс, получайте своевременные уведомления и управляйте задачами в режиме реального времени — просто и эффективно.
                    </div>

                    <div class="portal-features">
                        <div class="feature-item">Интуитивная Kanban-доска с поддержкой drag and drop для удобного и быстрого перемещения задач между колонками</div>
                        <div class="feature-item">Поддержка до 14 статусов для гибкого управления этапами выполнения задач</div>
                        <div class="feature-item">Система мгновенных уведомлений через удобный виджет, отображающая важные события и изменения в задачах в реальном времени</div>
                        <div class="feature-item">Расширенная аналитика для подробного анализа продуктивности и эффективности команды</div>
                        <div class="feature-item">Полноценная мобильная версия для работы и контроля задач в любом месте и в любое время</div>
                        <div class="feature-item">Обновления в режиме реального времени без необходимости ручного обновления страницы</div>
                        <div class="feature-item">Детальная история изменений каждой задачи для прозрачности и аудита</div>
                        <div class="feature-item">Встроенные комментарии для оперативного взаимодействия и обсуждений внутри задач</div>

                     </div>

                    <a href="https://its.tez-tour.com" class="portal-link">
                        Открыть TEZ Navigator
                    </a>

                    <p style="font-size: 12px; color: #6c757d; margin-top: 15px;">
                        Используйте ваш аккаунт TEZ ERP для входа в систему
                    </p>
                </div>
            </div>

            <div class="footer">
                <p>© 2026 TEZ TOUR. Все права защищены.</p>
                <p>Это автоматическое сообщение системы технической поддержки.</p>
            </div>
        </div>
    </body>
    </html>
    '''

def template_html_Assigned_vln(issueID, body, strParam, oldParam, newParam, dateCreated, title, author, status, priority, assigned, add_notes=None):
    # Преобразуем add_notes в строку, если None
    add_notes = add_notes if add_notes is not None else ""
    body = body if body is not None else ""  # На всякий случай проверяем body

    # Формируем блок с комментариями, если add_notes не пустой
    notes_html = ""
    if add_notes:
        notes_html = (
            '<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border: 1px solid #d1cdc7; margin-top: 20px;">'
            '<tr>'
            '<td align="left" style="background-color: #eae7e9; border-left: 5px solid #d1cdc7; padding: 10px 10px 10px 10px;">'
            '<div style="font-family: monospace; font-size: 40px; color: #d1cdc7; margin-bottom: -50px;">“</div>'
            '<div style="font-family: monospace; font-size: 14px; color: #252525; line-height: 18px; padding: 10px 10px 10px 40px;">'
            '<p style="color: #808080; font-style: italic; margin: 0;">Комментарий исполнителя: ' + add_notes + '</p>'
            '</div>'
            '<div style="font-family: monospace; font-size: 40px; color: #d1cdc7; line-height: 18px;">”</div>'
            '</td>'
            '</tr>'
            '</table>'
        )

    # Основной HTML-шаблон
    html = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style>
    body { margin: 0; padding: 0; width: 100%; height: 100%; font-family: Tahoma, Verdana, Arial, sans-serif; font-size: 14px; color: #252525; }
    a { color: #007bff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    table { border-collapse: collapse; }
    .content { line-height: 18px; }
    .content pre { font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #000000; line-height: 16px; white-space: pre-wrap; }
    .footer-note { text-align: justify; font-size: 12px; font-style: italic; text-decoration: underline; }
</style>
</head>
<body>
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td align="center" valign="top" bgcolor="#ecd8bf" style="padding: 20px;">
    <table width="700" border="1" cellspacing="0" cellpadding="0">
    <tr align="top">
    <td bgcolor="#f1eff0" style="padding: 20px 10px 20px 10px;">
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
        <td style="width: 350px;" width="350" bgcolor="#f1eff0" align="left">
            <!-- Закомментирован логотип -->
            <!-- <img src="https://s.tez-tour.com/article/7025866/TEZ_TOUR_logo_horizontal_cmyk_7505.png" alt="TEZ TOUR" title="TEZ TOUR" style="width: 200px;" width="200" border="0"> -->
        </td>
        <td align="right" bgcolor="#f1eff0" width="400">
            <div style="font-size: 14px; color: #252525; padding: 0; line-height: 18px;">
                <b>Служба технической поддержки TEZ TOUR</b><br>
                Email: <a href="mailto:help@tez-tour.com" target="_blank">help@tez-tour.com</a><br>
                <img src="http://s.tez-tour.com/article/7024808/line_300x1_4073.gif" alt="" width="700" height="0" border="0">
            </div>
        </td>
        </tr>
        </table>

        <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr><td style="border-bottom: 1px solid #d1cdc7;"> </td></tr>
        <tr><td> </td></tr>
        </table>

        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin: 10px 0px 10px 0px;">
        <tr>
        <td align="left" bgcolor="#f1eff0">
            <div class="content">
                Задача #''' + issueID + ''' была обновлена <br><br>
                <table cellspacing="0">
                <tr>
                    <td>  • </td>
                    <td><b>''' + strParam + '</b> изменился с <b>''' + oldParam + '''</b> на <b>''' + newParam + '''</b></td>
                </tr>
                </table>
                <br>
                <a href="https://helpdesk.teztour.com/issues/''' + issueID + '''"><strong>Задача #''' + issueID + ''': ''' + title + '''</strong></a><br>
                <br>
                <table cellspacing="0">
                <tr><td>  • Автор:</td><td>''' + author + '''</td></tr>
                <tr><td>  • Статус:</td><td>''' + status + '''</td></tr>
                <tr><td>  • Приоритет:</td><td>''' + priority + '''</td></tr>
                <tr><td>  • Исполнитель:</td><td>''' + assigned + '''</td></tr>
                <tr><td>  • Дата создания:</td><td>''' + dateCreated + '''</td></tr>
                </table>
                <div class="content">
                    <pre>''' + body + '''</pre>
                </div>
                ''' + notes_html + '''
                <br><br>
                <p class="footer-note">
                    Это автоматическое сообщение. Пожалуйста, дождитесь нашего ответа и не создавайте новые заявки, отправляя письма на
                    <a href="mailto:help@tez-tour.com" target="_blank">help@tez-tour.com</a>, так как это может увеличить время обработки вашего запроса. При ответах, пожалуйста, не изменяйте тему письма.
                </p>
                <p>
                    Вы также можете посмотреть и обработать свои заявки, зарегистрировавшись на ресурсе
                    <a href="https://its.tez-tour.com">https://its.tez-tour.com</a> с использованием вашего аккаунта TEZ ERP.
                </p>
            </div>
        </td>
        </tr>
        </table>
    </td>
    </tr>
    </table>
</td>
</tr>
</table>
</body>
</html>
'''
    return html
