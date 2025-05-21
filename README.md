
# 🧪 Example Lab – Laboratorios de Redes con Containerlab

Este repositorio contiene un par de laboratorios prácticos de redes, orientados a entornos de pruebas con firewalls, segmentación de red y automatización de configuraciones. Está diseñado con fines educativos y de experimentación técnica como un previo a nuestro proyecto final de prácticas en el equipo de Redes de Kyndryl, empleando tecnologías actuales como **Containerlab**, **FortiOS**, **Palo Alto PAN-OS** y **Python**.



## 🚀 Tecnologías utilizadas

- 🐍 **Python** (automatización de configuraciones)
- 🧱 **Containerlab** (simulación de topologías en contenedores)
- 🔒 **FortiOS** (Firewall FortiGate)
- 🔥 **PAN-OS** (Firewall Palo Alto PA-VM)
- 🐧 Hosts Linux Alpine
- 🖧 VLANs, zonas de seguridad y filtrado de tráfico


## 🧩 Laboratorios disponibles

### `lab-dmz-interna`

Entorno completo que simula una infraestructura segmentada para un pequeño hospital 🏥

- 🔐 Firewalls en serie (FortiGate + Palo Alto)
- 🌐 DMZ con servidor web
- 🧬 Red interna con servidor LDAP, servidor Samba y cliente
- 🚦 Políticas de filtrado de tráfico aplicadas
- 📜 Configuraciones iniciales automatizadas

### `lab-solo-firewall-Forti-PaloAlto`

Laboratorio mínimo para pruebas individuales de los firewalls:

- Verificación de arranque y acceso
- Para pruebas rápidas y validación de imágenes


## 👩‍💻 Autoría

📡 Bajo la firma de **Laolink Consulting**, Proyecto desarrollado por **Laura Ramos Granados** y **Oleg Fernández-Llebrez Rodríguez** como parte de su formación en CGS ASIR.
