import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Item {
    id: combatScreen
    
    // Beautiful gradient background
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { 
                position: 0.0
                color: Qt.rgba(255/255, 107/255, 107/255, 1.0) // #ff6b6b
            }
            GradientStop { 
                position: 1.0
                color: Qt.rgba(255/255, 167/255, 38/255, 1.0) // #ffa726
            }
        }
    }
    
    ScrollView {
        anchors.fill: parent
        anchors.margins: 20
        
        Column {
            width: parent.width
            spacing: 20
            
            // Header
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "⚡ COMBATE"
                font.pixelSize: 36
                font.bold: true
                color: "#ffffff"
                
                DropShadow {
                    anchors.fill: parent
                    source: parent
                    radius: 8
                    samples: 16
                    color: Qt.rgba(0, 0, 0, 0.5)
                }
            }
            
            // Quick Status Card
            Rectangle {
                width: parent.width
                height: 120
                radius: 20
                color: Qt.rgba(142/255, 68/255, 173/255, 0.9)
                
                Row {
                    anchors.centerIn: parent
                    spacing: 40
                    
                    Column {
                        spacing: 5
                        Text {
                            text: "Vida"
                            font.pixelSize: 18
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        Text {
                            text: character.hpCurrent + "/" + character.hpMax
                            font.pixelSize: 24
                            color: "#e74c3c"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }
                    
                    Column {
                        spacing: 5
                        Text {
                            text: "Esperanza"
                            font.pixelSize: 18
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        Text {
                            text: character.hope
                            font.pixelSize: 24
                            color: "#27ae60"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }
                    
                    Column {
                        spacing: 5
                        Text {
                            text: "Armadura"
                            font.pixelSize: 18
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        Text {
                            text: character.armor
                            font.pixelSize: 24
                            color: "#95a5a6"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }
                }
            }
            
            // Combat Actions Card
            Rectangle {
                width: parent.width
                height: actionsColumn.height + 40
                radius: 20
                color: Qt.rgba(44/255, 62/255, 80/255, 0.9)
                
                Column {
                    id: actionsColumn
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "Acciones de Combate"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    GridLayout {
                        width: parent.width
                        columns: 2
                        rowSpacing: 15
                        columnSpacing: 15
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 60
                            text: "⚔️ Ataque con Arma"
                            backgroundColor: "#e74c3c"
                            hoverColor: "#c0392b"
                            onClicked: console.log("Weapon attack")
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 60
                            text: "🔮 Lanzar Hechizo"
                            backgroundColor: "#9b59b6"
                            hoverColor: "#8e44ad"
                            onClicked: console.log("Cast spell")
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 60
                            text: "🛡️ Defensa"
                            backgroundColor: "#3498db"
                            hoverColor: "#2980b9"
                            onClicked: console.log("Defend")
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 60
                            text: "🏃 Acción Especial"
                            backgroundColor: "#f39c12"
                            hoverColor: "#d68910"
                            onClicked: console.log("Special action")
                        }
                    }
                }
            }
            
            // Placeholder
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "🚧 Sistema de combate en desarrollo..."
                font.pixelSize: 18
                color: "#ffffff"
                opacity: 0.7
            }
        }
    }
}
