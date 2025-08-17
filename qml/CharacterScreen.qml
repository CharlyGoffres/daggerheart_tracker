import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: characterScreen
    
    // Beautiful gradient background
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { 
                position: 0.0
                color: Qt.rgba(168/255, 237/255, 234/255, 1.0) // #a8edea
            }
            GradientStop { 
                position: 1.0
                color: Qt.rgba(254/255, 214/255, 227/255, 1.0) // #fed6e3
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
                text: "⚔️ FICHA DE PERSONAJE"
                font.pixelSize: 36
                font.bold: true
                color: "#ffffff"
                
            }
            
            // Character Info Card
            Rectangle {
                width: parent.width
                height: 200
                radius: 20
                color: Qt.rgba(44/255, 62/255, 80/255, 0.9)
                
                Column {
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "Información del Personaje"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    GridLayout {
                        width: parent.width
                        columns: 2
                        rowSpacing: 10
                        columnSpacing: 15
                        
                        Text { text: "Nombre:"; color: "#bdc3c7"; font.pixelSize: 16 }
                        TextField {
                            Layout.fillWidth: true
                            text: character.name
                            onTextChanged: character.name = text
                            background: Rectangle { radius: 8; color: "#34495e" }
                            color: "#ecf0f1"
                        }
                        
                        Text { text: "Clase:"; color: "#bdc3c7"; font.pixelSize: 16 }
                        TextField {
                            Layout.fillWidth: true
                            text: character.className
                            onTextChanged: character.className = text
                            background: Rectangle { radius: 8; color: "#34495e" }
                            color: "#ecf0f1"
                        }
                        
                        Text { text: "Nivel:"; color: "#bdc3c7"; font.pixelSize: 16 }
                        SpinBox {
                            Layout.fillWidth: true
                            value: character.level
                            from: 1
                            to: 20
                            onValueChanged: character.level = value
                        }
                    }
                }
            }
            
            // Health Card
            Rectangle {
                width: parent.width
                height: 150
                radius: 20
                color: Qt.rgba(192/255, 57/255, 43/255, 0.9)
                
                Column {
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "❤️ Salud y Recursos"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    Row {
                        anchors.horizontalCenter: parent.horizontalCenter
                        spacing: 20
                        
                        Text {
                            text: "Puntos de Vida:"
                            font.pixelSize: 18
                            color: "#ecf0f1"
                        }
                        
                        SpinBox {
                            value: character.hpCurrent
                            from: 0
                            to: 999
                            onValueChanged: character.hpCurrent = value
                        }
                        
                        Text {
                            text: "/"
                            font.pixelSize: 24
                            color: "#ecf0f1"
                        }
                        
                        SpinBox {
                            value: character.hpMax
                            from: 1
                            to: 999
                            onValueChanged: character.hpMax = value
                        }
                    }
                }
            }
            
            // Placeholder for more character features
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "🚧 Más características próximamente..."
                font.pixelSize: 18
                color: "#ffffff"
                opacity: 0.7
            }
        }
    }
}
