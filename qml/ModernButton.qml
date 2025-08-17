import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: modernButton
    
    property color backgroundColor: "#3498db"
    property color hoverColor: "#2980b9"
    property color pressedColor: "#1f5f8b"
    property color textColor: "#ffffff"
    property int fontSize: 16
    property bool roundedCorners: true
    
    // Raspberry Pi touch optimizations
    property bool isSmallScreen: parent && parent.width <= 800
    property real minTouchSize: isSmallScreen ? 60 : 44
    
    // Ensure minimum touch target size for RPi touchscreens
    property real preferredWidth: Math.max(implicitContentWidth + 20, minTouchSize)
    property real preferredHeight: Math.max(implicitContentHeight + 20, minTouchSize)
    
    background: Rectangle {
        id: buttonBackground
        radius: modernButton.roundedCorners ? (isSmallScreen ? 12 : 15) : 0
        color: modernButton.pressed ? modernButton.pressedColor : 
               (modernButton.hovered ? modernButton.hoverColor : modernButton.backgroundColor)
        
        // Add subtle border for better visibility on RPi screens
        border.width: isSmallScreen ? 1 : 0
        border.color: Qt.rgba(1, 1, 1, 0.2)
        
        Behavior on color {
            ColorAnimation {
                duration: settings.animationsEnabled ? 150 : 0
                easing.type: Easing.OutQuad
            }
        }
    }
    
    contentItem: Text {
        text: modernButton.text
        font.pixelSize: isSmallScreen ? Math.max(modernButton.fontSize * 0.9, 12) : modernButton.fontSize
        font.bold: true
        color: modernButton.textColor
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        wrapMode: Text.Wrap
    }
    
    // Scale animation
    scale: pressed ? 0.95 : (hovered ? 1.05 : 1.0)
    
    Behavior on scale {
        PropertyAnimation {
            duration: settings.animationsEnabled ? 100 : 0
            easing.type: Easing.OutQuad
        }
    }
}
