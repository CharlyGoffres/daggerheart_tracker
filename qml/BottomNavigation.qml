import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    id: bottomNav
    color: Qt.rgba(0, 0, 0, 0.8)
    
    signal screenRequested(string screenName)
    
    property string currentScreen: "rolls"
    property var buttons: ["rolls", "character", "combat", "settings"]
    // Raspberry Pi optimized dice icons using Unicode dice symbols
    property var buttonIcons: ["⚀⚁", "⚔️", "⚡", "⚙️"]
    property var buttonLabels: ["Dados", "Personaje", "Combate", "Config"]
    
    // Raspberry Pi touch-friendly sizing
    property real iconSize: width < 800 ? 20 : 24  // Smaller icons for RPi 7" screen
    property real textSize: width < 800 ? 10 : 12  // Smaller text for RPi
    property real buttonSpacing: width < 800 ? 2 : 4  // Tighter spacing on small screens
    
    RowLayout {
        anchors.fill: parent
        spacing: 0
        
        Repeater {
            model: bottomNav.buttons
            
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: currentScreen === modelData ? Qt.rgba(1, 1, 1, 0.2) : "transparent"
                
                // Add subtle border for better visibility on RPi screens
                border.color: currentScreen === modelData ? Qt.rgba(1, 1, 1, 0.3) : "transparent"
                border.width: 1
                radius: 4
                
                Column {
                    anchors.centerIn: parent
                    spacing: bottomNav.buttonSpacing
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: bottomNav.buttonIcons[index]
                        font.pixelSize: bottomNav.iconSize
                        color: "#ffffff"
                        // Enhanced text rendering for better clarity on RPi
                        renderType: Text.NativeRendering
                        font.bold: currentScreen === modelData
                    }
                    
                    Text {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: bottomNav.buttonLabels[index]
                        font.pixelSize: bottomNav.textSize
                        color: "#ffffff"
                        opacity: currentScreen === modelData ? 1.0 : 0.8
                        renderType: Text.NativeRendering
                    }
                }
                
                MouseArea {
                    anchors.fill: parent
                    // Larger touch area for RPi touchscreens
                    anchors.margins: -2
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
