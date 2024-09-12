import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

# Configuración del servidor SMTP 
smtp_host = ""
smtp_port = 587
smtp_user = ""
smtp_password = ""

# Configuración del correo
from_address = 'TicoDevs Software Solutions<contacto@consultoresinfinito.info>'
from_name = 'TicoDevs Software Solutions 🏢'
subject = 'Información de Servicios 📲'
body = '''
<div style="text-align: center;">
    <img src="https://ticodevscr.com/wp-content/uploads/2024/09/LogoTicoDevs.png" alt="LogoTicoDevs" width="300px" />
    <h2>Impulsa el Éxito de Tu Empresa con Soluciones Tecnológicas Avanzadas ✅</h2> 
    <p>Estimado equipo,<br /> Esperamos que este mensaje les encuentre bien y con sus proyectos avanzando con éxito.<br /> 
    Me presento: soy José Pablo Mendez Poveda, gerente de TicoDevs Software Solutions, y me gustaría compartir con ustedes los servicios especializados que ofrecemos,<br /> 
    diseñados específicamente para optimizar la eficiencia administrativa y operativa mediante la implementación de innovación tecnológica de vanguardia. </p> 
    <h3><strong>Tu Socio en Outsourcing de IT, Desarrollo de Software Personalizado y Gestión Tecnológica</strong></h3> 
    <p>En el entorno actual, la gestión administrativa precisa, la operación continua y la integración tecnológica son esenciales para el éxito de cualquier empresa.<br /> 
    Nos especializamos en ofrecer soluciones integrales en estas áreas clave, adaptadas a las necesidades y objetivos específicos de su organización.<br /> 
    Nuestro enfoque colaborativo y personalizado garantiza una transición fluida y una mejora continua alineada con los valores y metas de su empresa. </p> 
    <h3><strong>Descubre Cómo Potenciar Tu Empresa con Nuestro Soporte Tecnológico Integral</strong></h3> 
    <p>Estamos convencidos de que nuestros servicios pueden aportar un gran valor a su empresa.<br /> </p> 
    <p>Si está interesado en dar el siguiente paso, no dude en hacer clic en el botón de abajo para iniciar una conversación ahora mismo.</p>
    <p>Estaremos encantados de responder a todas sus preguntas y proporcionarle una consulta para discutir sus necesidades específicas.</p> 
    <p>Gracias por considerarnos como su socio de confianza en tecnología y gestión administrativa.</p> 
    <p>Esperamos la oportunidad de colaborar y contribuir al crecimiento y éxito de su empresa.</p>

    <div style="display: inline; justify-content: center; margin-top: 2rem; ">
        <a href="https://wa.link/zlbbfc" style="text-decoration: none;">
            <button style="padding: 15px; border-radius: 50px; background-color: #25D366; color: #fff; font-weight: 600; border: none; ">Iniciar Chat 👋</button>
        </a>

        <a href="https://ticodevscr.com" style="text-decoration: none;">
            <button style=" margin-left: 2rem; padding: 15px; border-radius: 50px; background-color: #0B4E82; color: #fff; font-weight: 600; border: none; ">Sitio Web 🌐</button>
        </a>
    </div>

    <footer style="margin-top: 1rem;">
        <hr style="border-color: #0B4E82; border-width: 2px;" />
    </footer>

    <div style="display: inline-flex; justify-content: center;">
        <a style="width: 50px;
        height: 50px;
        border-radius: 10%;
        margin: 15px 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 24px;
        text-decoration: none;
        background-color: #1877f2;
        " href="https://www.facebook.com/profile.php?id=61554129052610&mibextid=YMEMSu">
            <img src="https://ticodevscr.com/wp-content/uploads/2024/09/LogoFacebook.png" width="50px" alt="FacebookImg" />
        </a>
        <a style="width: 50px;
        height: 50px;
        border-radius: 10%;
        margin: 15px 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 24px;
        text-decoration: none;
        background-color: #e4405f;
        " href="https://www.instagram.com/ticodevscr?igsh=MXZ2c3BwejkwZHRodg==">
            <img src="https://ticodevscr.com/wp-content/uploads/2024/09/LogoInstagram.png" width="50px" alt="InstagramImg" />
        </a>
        <a style="width: 50px;
        height: 50px;
        border-radius: 10%;
        margin: 15px 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 24px;
        text-decoration: none;
        background-color: #0077b5;
        " href="https://www.linkedin.com/in/tico-devs-53b2aa2b3">
            <img src="https://ticodevscr.com/wp-content/uploads/2024/09/LogoLinkedin.png" width="50px" alt="LinkedImg" />
        </a>
    </div>
</div>
'''

# Lista de destinatarios
recipients = [
    'josemendez@ticodevscr.com',
]

# Enviar correo a cada destinatario
batch_size = 25
unique_recipients = list(set(recipients))

for i in range(0, len(unique_recipients), batch_size):
    batch = unique_recipients[i:i + batch_size]
    
    for recipient in batch:
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))

            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(from_address, recipient, msg.as_string())

            print(f'El Mensaje fue enviado a {recipient}')
            with open('Enviados.txt', 'a') as log_file:
                log_file.write(f'Correo enviado a: {recipient}\n')

        except Exception as e:
            print(f'Error al enviar correo a {recipient}: {e}')
            with open('Fallados.txt', 'a') as log_file:
                log_file.write(f'{e}\n')

    sleep(1)  
