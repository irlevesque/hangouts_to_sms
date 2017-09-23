#!/usr/bin/env python3
import argparse
from hangouts_parser import HangoutsParser
from titanium_backup_formatter import TitaniumBackupFormatter

parser = argparse.ArgumentParser()
parser.add_argument(
    '--phone-number', type=str, required=True,
    help='your phone number, including country code')
parser.add_argument(
    '--hangouts-file', default='Hangouts.json')
parser.add_argument(
    '--output-file', default='messages.xml')
args = parser.parse_args()

# Parse the Hangouts data and output Titanium Backup XML
hangouts_parser = HangoutsParser()
titanium_output = TitaniumBackupFormatter()
print("Parsing Hangouts data file...")
conversations, self_gaia_id = hangouts_parser.parse_input_file(
    args.hangouts_file, args.phone_number)
print("Done.")
print("Converting to SMS export file...")
titanium_output.create_output_file(
    conversations, self_gaia_id, args.output_file)
print("Done.")
