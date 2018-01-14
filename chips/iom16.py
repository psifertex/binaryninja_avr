import binaryninja_avr.chips


class IOM16(binaryninja_avr.chips.Chip):
    """
    ATMega16
    """

    CHIP_ALIASES = ["iom16", "ATMega16"]
    RAM_SIZE = 1024
    ROM_SIZE = 16 * 1024
    INTERRUPT_VECTOR_SIZE = 4

    IO_REGISTERS = {
        0x00: 'TWBR',
        0x01: 'TWSR',
        0x02: 'TWAR',
        0x03: 'TWDR',
        0x04: 'ADCL',
        0x05: 'ADCH',
        0x06: 'ADCSRA',
        0x07: 'ADMUX',
        0x08: 'ACSR',
        0x09: 'UBRRL',
        0x0A: 'UCSRB',
        0x0B: 'UCSRA',
        0x0C: 'UDR',
        0x0D: 'SPCR',
        0x0E: 'SPSR',
        0x0F: 'SPDR',
        0x10: 'PIND',
        0x11: 'DDRD',
        0x12: 'PORTD',
        0x13: 'PINC',
        0x14: 'DDRC',
        0x15: 'PORTC',
        0x16: 'PINB',
        0x17: 'DDRB',
        0x18: 'PORTB',
        0x19: 'PINA',
        0x1A: 'DDRA',
        0x1B: 'PORTA',
        0x1C: 'EECR',
        0x1D: 'EEDR',
        0x1E: 'EEARL',
        0x1F: 'EEARH',
        0x20: 'UBRRH',
        0x20: 'UCSRC',
        0x21: 'WDTCR',
        0x22: 'ASSR',
        0x23: 'OCR2',
        0x24: 'TCNT2',
        0x25: 'TCCR2',
        0x26: 'ICR1L',
        0x27: 'ICR1H',
        0x28: 'OCR1BL',
        0x29: 'OCR1BH',
        0x2A: 'OCR1AL',
        0x2B: 'OCR1AH',
        0x2C: 'TCNT1L',
        0x2D: 'TCNT1H',
        0x2E: 'TCCR1B',
        0x2F: 'TCCR1A',
        0x30: 'SFIOR',
        0x31: 'OSCCAL',
        0x31: 'OCDR',
        0x32: 'TCNT0',
        0x33: 'TCCR0',
        0x34: 'MCUCSR',
        0x35: 'MCUCR',
        0x36: 'TWCR',
        0x37: 'SPMCSR',
        0x38: 'TIFR',
        0x39: 'TIMSK',
        0x3A: 'GIFR',
        0x3B: 'GICR',
        0x3C: 'OCR0',
        0x3D: 'SPL',
        0x3E: 'SPH',
        0x3F: 'SREG',
    }

    INTERRUPT_VECTORS = [
        'RESET_vect',
        'INT0_vect',
        'INT1_vect',
        'TIMER2_COMP_vect',
        'TIMER2_OVF_vect',
        'TIMER1_CAPT_vect',
        'TIMER1_COMPA_vect',
        'TIMER1_COMPB_vect',
        'TIMER1_OVF_vect',
        'TIMER0_OVF_vect',
        'SPI_STC_vect',
        'USART_RXC_vect',
        'USART_UDRE_vect',
        'USART_TXC_vect',
        'ADC_vect',
        'EE_RDY_vect',
        'ANA_COMP_vect',
        'TWI_vect',
        'INT2_vect',
        'TIMER0_COMP_vect',
        'SPM_RDY_vect',
    ]

    # TODO: Notice the hole between the IO_REGS and the eIO_REGS of 0x20. This
    # is exactly the space for R0-R31, the IO_REGS will be mapped at +0x20. This
    # is somewhat misleading and should be fixed.
    EXTENDED_IO_REGISTERS = {
        0x60: 'WDTCSR',
        0x61: 'CLKPR',
        0x64: 'PRR0',
        0x65: 'PRR1',
        0x66: 'OSCCAL',
        0x67: 'RCCTRL',
        0x68: 'PCICR',
        0x69: 'EICRA',
        0x6A: 'EICRB',
        0x6B: 'PCMSK0',
        0x6E: 'TIMSK0',
        0x6F: 'TIMSK1',
        0x71: 'TIMSK3',
        0x72: 'TIMSK4',
        0x78: 'ADCL',
        0x79: 'ADCH',
        0x7A: 'ADCSRA',
        0x7B: 'ADCSRB',
        0x7C: 'ADMUX',
        0x7D: 'DIDR2',
        0x7E: 'DIDR0',
        0x7F: 'DIDR1',
        0x80: 'TCCR1A',
        0x81: 'TCCR1B',
        0x82: 'TCCR1C',
        0x84: 'TCNT1L',
        0x85: 'TCNT1H',
        0x86: 'ICR1L',
        0x87: 'ICR1H',
        0x88: 'OCR1AL',
        0x89: 'OCR1AH',
        0x8A: 'OCR1BL',
        0x8B: 'OCR1BH',
        0x8C: 'OCR1CL',
        0x8D: 'OCR1CH',
        0x90: 'TCCR3A',
        0x91: 'TCCR3B',
        0x92: 'TCCR3C',
        0x94: 'TCNT3L',
        0x95: 'TCNT3H',
        0x96: 'ICR3L',
        0x97: 'ICR3H',
        0x98: 'OCR3AL',
        0x99: 'OCR3AH',
        0x9A: 'OCR3BL',
        0x9B: 'OCR3BH',
        0x9C: 'OCR3CL',
        0x9D: 'OCR3CH',
        0xB8: 'TWBR',
        0xB9: 'TWSR',
        0xBA: 'TWAR',
        0xBB: 'TWDR',
        0xBC: 'TWCR',
        0xBD: 'TWAMR',
        0xBE: 'TCNT4',
        0xBF: 'TC4H',
        0xC0: 'TCCR4A',
        0xC1: 'TCCR4B',
        0xC2: 'TCCR4C',
        0xC3: 'TCCR4D',
        0xC4: 'TCCR4E',
        0xC5: 'CLKSEL0',
        0xC6: 'CLKSEL1',
        0xC7: 'CLKSTA',
        0xC8: 'UCSR1A',
        0xC9: 'UCSR1B',
        0xCA: 'UCSR1C',
        0xCB: 'UCSR1D',
        0xCC: 'UBRR1L',
        0xCD: 'UBRR1H',
        0xCE: 'UDR1',
        0xCF: 'OCR4A',
        0xD0: 'OCR4B',
        0xD1: 'OCR4C',
        0xD2: 'OCR4D',
        0xD4: 'DT4',
        0xD7: 'UHWCON',
        0xD8: 'USBCON',
        0xD9: 'USBSTA',
        0xDA: 'USBINT',
        0xE0: 'UDCON',
        0xE1: 'UDINT',
        0xE2: 'UDIEN',
        0xE3: 'UDADDR',
        0xE4: 'UDFNUML',
        0xE5: 'UDFNUMH',
        0xE6: 'UDMFN',
        0xE8: 'UEINTX',
        0xE9: 'UENUM',
        0xEA: 'UERST',
        0xEB: 'UECONX',
        0xEC: 'UECFG0X',
        0xED: 'UECFG1X',
        0xEE: 'UESTA0X',
        0xEF: 'UESTA1X',
        0xF0: 'UEIENX',
        0xF1: 'UEDATX',
        0xF2: 'UEBCLX',
        0xF3: 'UEBCHX',
        0xF4: 'UEINT',
    }