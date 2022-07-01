(ns notebooks.notebooks
  (:require [nextjournal.clerk :as clerk]))

;;; Clerk demo: https://github.com/nextjournal/clerk#-using-clerk
;;; see notebooks: https://github.com/nextjournal/clerk/blob/main/notebooks
;;; - these notebooks have been copied to src/clojure_experiments/visualizations/clerk/notebooks/
(comment
;; start Clerk's buit-in webserver on the default port 7777,
;; opening the browser when done
  (clerk/serve! {:browse? true})

;; let Clerk watch the given `:paths` for changes
  #_(clerk/serve! {:watch-paths ["notebooks" "src"]})
  (clerk/serve! {:watch-paths ["src/notebooks"]})

  .)

