int analogPin = A0;    

#Variável para armazenar o valor lido
 int val = 0;          

void setup()
{
#Inicia o monitor Serial.
 Serial.begin(9600);         
}

void loop()
{

# Leitura do pino analogico
 val = analogRead(analogPin);   
 Serial.println(val);

}