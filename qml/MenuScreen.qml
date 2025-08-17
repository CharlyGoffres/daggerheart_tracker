import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: menuScreen
    
    ScrollView {
        anchors.fill: parent
        anchors.margins: 20
        
        Column {
            width: parent.width
            spacing: 30
            
            // Header
            Item {
                width: parent.width
                height: 200
                
                Column {
                    anchors.centerIn: parent
                    spacing: 20
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "DAGGERHEART\n⚔️ TRACKER ⚔️"
                        font.pixelSize: 48
                        font.bold: true
                        color: "#ffffff"
                        horizontalAlignment: Text.AlignHCenter
                    }
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "Tu compañero de aventuras definitivo"
                        font.pixelSize: 18
                        color: "#ecf0f1"
                        opacity: 0.9
                    }
                }
            }
            
            // Navigation Cards
            Column {
                width: parent.width
                spacing: 20
                
                MenuCard {
                    title: "🎲 Tiradas de Dados"
                    subtitle: "Realiza tiradas con ventajas y modificadores"
                    cardColor: "#e74c3c"
                    onClicked: stackView.parent.switchToScreen("rolls")
                }
                
                MenuCard {
                    title: "⚔️ Ficha de Personaje"
                    subtitle: "Gestiona stats, vida y habilidades"
                    cardColor: "#27ae60"
                    onClicked: stackView.parent.switchToScreen("character")
                }
                
                MenuCard {
                    title: "⚡ Combate"
                    subtitle: "Ataques, hechizos y gestión de recursos"
                    cardColor: "#f39c12"
                    onClicked: stackView.parent.switchToScreen("combat")
                }
                
                MenuCard {
                    title: "⚙️ Configuración"
                    subtitle: "Personaliza tu experiencia"
                    cardColor: "#8e44ad"
                    onClicked: stackView.parent.switchToScreen("settings")
                }
            }
            
            // Exit Button
            Item {
                width: parent.width
                height: 80
                
                ModernButton {
                    anchors.centerIn: parent
                    width: 200
                    height: 50
                    text: "💀 Salir del Juego"
                    backgroundColor: "#c0392b"
                    hoverColor: "#a93226"
                    
                    onClicked: app.exitApp()
                }
            }
        }
    }
}
