# app/anonymizer.py

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json

def anonymize_text(text_to_anonymize):
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    analyzer_results = analyzer.analyze(text=text_to_anonymize, language="en")

    anonymized_results = anonymizer.anonymize(
        text=text_to_anonymize,
        analyzer_results=analyzer_results,
        operators={"DEFAULT": OperatorConfig("replace", {"new_value": "XXX"})},
    )
    return(json.loads(anonymized_results.to_json())['text'])