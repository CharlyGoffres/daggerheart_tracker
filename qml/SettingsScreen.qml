import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: settingsScreen
    
    // Responsive properties for 16:9 optimization
    readonly property bool isWideScreen: width > height && width > 1200
    readonly property int headerHeight: isWideScreen ? 80 : 60
    readonly property int cardPadding: isWideScreen ? 30 : 20
    
    // Beautiful gradient background
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { 
                position: 0.0
                color: Qt.rgba(255/255, 236/255, 210/255, 1.0) // #ffecd2
            }
            GradientStop { 
                position: 1.0
                color: Qt.rgba(252/255, 182/255, 159/255, 1.0) // #fcb69f
            }
        }
    }
    
    ScrollView {
        anchors.fill: parent
        anchors.margins: isWideScreen ? 40 : 20
        
        Item {
            width: settingsScreen.width - (isWideScreen ? 80 : 40)
            height: contentColumn.height
            
            Column {
                id: contentColumn
                anchors.horizontalCenter: parent.horizontalCenter
                width: Math.min(parent.width, isWideScreen ? 1400 : 1200)
                spacing: isWideScreen ? 30 : 20
        
        Column {
            width: parent.width
            spacing: 20
            
            // Header with responsive design
            Row {
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 20
                height: headerHeight
                
                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    text: "⚙️ CONFIGURACIÓN"
                    font.pixelSize: isWideScreen ? 42 : 36
                    font.bold: true
                    color: "#ffffff"
                }
            }
            
            // Main content area for wide screens
            Item {
                width: parent.width
                height: isWideScreen ? Math.max(leftCard.height, rightCard.height) : 
                        leftCard.height + rightCard.height + (isWideScreen ? 30 : 20)
                
                // App Settings Card
                Rectangle {
                    id: leftCard
                    width: isWideScreen ? (parent.width - 30) / 2 : parent.width
                    height: appSettingsColumn.height + (cardPadding * 2)
                    anchors.left: parent.left
                    anchors.top: parent.top
                    radius: 20
                    color: Qt.rgba(155/255, 89/255, 182/255, 0.9)
                    
                    Column {
                        id: appSettingsColumn
                        anchors.centerIn: parent
                        width: parent.width - (cardPadding * 2)
                        spacing: 15
                    
                    Text {
                        text: "📱 Configuración de la Aplicación"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    // Dark theme toggle
                    RowLayout {
                        width: parent.width
                        
                        Column {
                            Layout.fillWidth: true
                            Text {
                                text: "🎨 Tema Oscuro"
                                font.pixelSize: 18
                                color: "#ecf0f1"
                            }
                            Text {
                                text: "Usar colores oscuros para la interfaz"
                                font.pixelSize: 14
                                color: "#bdc3c7"
                            }
                        }
                        
                        Switch {
                            checked: settings.darkTheme
                            onCheckedChanged: settings.darkTheme = checked
                        }
                    }
                    
                    // Sounds toggle
                    RowLayout {
                        width: parent.width
                        
                        Column {
                            Layout.fillWidth: true
                            Text {
                                text: "🔊 Sonidos"
                                font.pixelSize: 18
                                color: "#ecf0f1"
                            }
                            Text {
                                text: "Reproducir efectos de sonido"
                                font.pixelSize: 14
                                color: "#bdc3c7"
                            }
                        }
                        
                        Switch {
                            checked: settings.soundsEnabled
                            onCheckedChanged: settings.soundsEnabled = checked
                        }
                    }
                    
                    // Animations toggle
                    RowLayout {
                        width: parent.width
                        
                        Column {
                            Layout.fillWidth: true
                            Text {
                                text: "✨ Animaciones"
                                font.pixelSize: 18
                                color: "#ecf0f1"
                            }
                            Text {
                                text: "Mostrar animaciones y transiciones"
                                font.pixelSize: 14
                                color: "#bdc3c7"
                            }
                        }
                        
                        Switch {
                            checked: settings.animationsEnabled
                            onCheckedChanged: settings.animationsEnabled = checked
                        }
                    }
                }
                
                // Game Settings Card
                Rectangle {
                    id: rightCard
                    width: isWideScreen ? (parent.width - 30) / 2 : parent.width
                    height: gameSettingsColumn.height + (cardPadding * 2)
                    anchors.right: parent.right
                    anchors.top: isWideScreen ? parent.top : leftCard.bottom
                    anchors.topMargin: isWideScreen ? 0 : 20
                    radius: 20
                    color: Qt.rgba(230/255, 126/255, 34/255, 0.9)
                    
                    Column {
                        id: gameSettingsColumn
                        anchors.centerIn: parent
                        width: parent.width - (cardPadding * 2)
                        spacing: 15
                    
                    Text {
                        text: "🎲 Configuración del Juego"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    // Auto save toggle
                    RowLayout {
                        width: parent.width
                        
                        Column {
                            Layout.fillWidth: true
                            Text {
                                text: "💾 Guardado Automático"
                                font.pixelSize: 18
                                color: "#ecf0f1"
                            }
                            Text {
                                text: "Guardar cambios automáticamente"
                                font.pixelSize: 14
                                color: "#bdc3c7"
                            }
                        }
                        
                        Switch {
                            checked: settings.autoSave
                            onCheckedChanged: settings.autoSave = checked
                        }
                    }
                    
                    // Dice speed slider
                    Column {
                        width: parent.width
                        spacing: 10
                        
                        Text {
                            text: "⚡ Velocidad de Dados: " + settings.diceSpeed + "%"
                            font.pixelSize: 18
                            color: "#ecf0f1"
                        }
                        
                        Slider {
                            width: parent.width
                            from: 10
                            to: 100
                            value: settings.diceSpeed
                            onValueChanged: settings.diceSpeed = Math.round(value)
                        }
                    }
                }
            }
            
            // Character Settings Card
            Rectangle {
                width: parent.width
                height: characterSettingsColumn.height + (cardPadding * 2)
                radius: 20
                color: Qt.rgba(39/255, 174/255, 96/255, 0.9)
                
                Column {
                    id: characterSettingsColumn
                    anchors.centerIn: parent
                    width: parent.width - (cardPadding * 2)
                    spacing: 15
                    
                    Text {
                        text: "⚔️ Configuración del Personaje"
                        font.pixelSize: isWideScreen ? 28 : 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    ModernButton {
                        anchors.horizontalCenter: parent.horizontalCenter
                        width: isWideScreen ? 240 : 200
                        height: isWideScreen ? 60 : 50
                        text: "🔄 Resetear Personaje"
                        backgroundColor: "#c0392b"
                        hoverColor: "#a93226"
                        onClicked: {
                            character.resetCharacter()
                            console.log("Character reset")
                        }
                    }
                }
            }
            
            // Version info
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Daggerheart Tracker v2.0 (Qt Edition)\nDesarrollado con ❤️ y QML"
                font.pixelSize: isWideScreen ? 16 : 14
                color: "#ffffff"
                opacity: 0.7
                horizontalAlignment: Text.AlignHCenter
            }
        }
    }
}
