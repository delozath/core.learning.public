#include <msp430.h>
#include <stdint.h>

unsigned char tx_data, rx_data;

void config();

void main(void){
  config();
  rx_data = 0;
  tx_data = 0;
  while (1){
    /*
    if (rx_data==10){
      tx_data = 0;
    }
    else{
        tx_data++;
    }*/
    tx_data++;
    __bis_SR_register(CPUOFF + GIE);
  }
}

void config(){
  WDTCTL = WDTPW + WDTHOLD;       // Stop WDT
  P1SEL |= BIT6 + BIT7;           // Config I2C pins to USCI_B0
  P1SEL2|= BIT6 + BIT7;

  UCB0CTL1  |= UCSWRST;           // Enable SW reset
  UCB0CTL0   = UCMODE_3 + UCSYNC; // I2C Slave, synchronous mode
  UCB0I2COA  = 50;                // I2C Address
  UCB0CTL1  &= ~UCSWRST;          // Clear SW reset, resume
  UCB0I2CIE |= UCSTTIE;           // Enable STT interrupt
  IE2       |= UCB0RXIE;          // Enable RX interrupt
}

#pragma vector = USCIAB0RX_VECTOR
__interrupt void USCIAB0RX(void){
  rx_data   = (unsigned int)UCB0RXBUF;
  UCB0TXBUF = tx_data;
  __bic_SR_register_on_exit(CPUOFF);
}

