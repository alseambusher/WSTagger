(ns lexical-analyzer.core
(use opennlp.nlp)
(use opennlp.treebank)
(use opennlp.tools.filters))
(def get-sentences (make-sentence-detector "models/en-sent.bin"))
(def tokenize (make-tokenizer "models/en-token.bin"))
(def detokenize (make-detokenizer "models/english-detokenizer.xml"))
(def pos-tag (make-pos-tagger "models/en-pos-maxent.bin"))
(def name-find (make-name-finder "models/namefind/en-ner-person.bin"))
(def chunker (make-treebank-chunker "models/en-chunker.bin"))

;;(deftest replace-me ;; FIXME: write
  ;;(is false "No tests have been written."))
(pprint (chunker (pos-tag (tokenize "The override system is meant to deactivate the accelerator when the brake pedal is pressed."))))
