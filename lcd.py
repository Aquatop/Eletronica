import I2C_LCD_driver
import time

# ïndices e parâmetros do aquário:
i = 1
ph = 7.5


lcdi2c = I2C_LCD_driver.lcd()
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()


# Exibe informações para a confirmação do token
#lcdi2c.lcd_display_string("Token gerado:", 1, 0)
#time.sleep(5)
lcdi2c.lcd_clear()
# Teste do token
# Quando o token for conferido pelo aplicativo, começa o loop de aferição dos parâmetros
while True:
    temperature = sensor.get_temperature()
    lcdi2c.lcd_display_string("Temp: %sC" %temperature, 1, 0)
    lcdi2c.lcd_display_string("pH: %1.2f" %ph, 2, 0)
    time.sleep(2)
    lcdi2c.lcd_clear()
    lcdi2c.lcd_display_string("Aquario: %d" %i, 1, 0)
    time.sleep(2)
    lcdi2c.lcd_clear()

