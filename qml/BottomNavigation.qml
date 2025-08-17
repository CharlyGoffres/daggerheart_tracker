import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Rectangle {
    id: bottomNav
    color: Qt.rgba(0, 0, 0, 0.8)
    
    signal screenRequested(string screenName)
    
    property string currentScreen: "menu"
    property var buttons: ["menu", "rolls", "character", "combat", "settings"]
    property var buttonIcons: ["🏠", "🎲", "⚔️", "⚡", "⚙️"]
    property var buttonLabels: ["Menú", "Dados", "Personaje", "Combate", "Config"]
    
    RowLayout {
        anchors.fill: parent
        spacing: 0
        
        Repeater {
            model: bottomNav.buttons
            
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: currentScreen === modelData ? Qt.rgba(1, 1, 1, 0.2) : "transparent"
                
                Column {
                    anchors.centerIn: parent
                    spacing: 4
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: bottomNav.buttonIcons[index]
                        font.pixelSize: 24
                        color: "#ffffff"
                    }
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: bottomNav.buttonLabels[index]
                        font.pixelSize: 12
                        color: "#ffffff"
                        opacity: 0.8
                    }
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        if (currentScreen !== modelData) {
                            currentScreen = modelData
                            bottomNav.screenRequested(modelData)
                        }
                    }
                    
                    onPressed: {
                        parent.color = Qt.rgba(1, 1, 1, 0.3)
                    }
                    
                    onReleased: {
                        parent.color = currentScreen === modelData ? Qt.rgba(1, 1, 1, 0.2) : "transparent"
                    }
                }
                
                // Ripple effect
                Rectangle {
                    id: ripple
                    anchors.centerIn: parent
                    width: 0
                    height: width
                    radius: width / 2
                    color: Qt.rgba(1, 1, 1, 0.3)
                    opacity: 0
                    
                    PropertyAnimation {
                        id: rippleAnimation
                        target: ripple
                        property: "width"
                        from: 0
                        to: parent.width * 1.5
                        duration: 300
                        easing.type: Easing.OutQuad
                    }
                    
                    PropertyAnimation {
                        id: rippleFade
                        target: ripple
                        property: "opacity"
                        from: 0.6
                        to: 0
                        duration: 300
                    }
                }
            }
        }
    }
}
