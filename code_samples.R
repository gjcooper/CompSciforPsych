# Commented code# {{{
#mRTs <- getMeanRTs(strats)
#annotation <- getAnnotations(strats)
#plotMeanRTS(mRTs, annotation)
#ggsave('MICs.png')
# }}}

# Indentation style# {{{
MIC <- function (strategy) {
	first.term <- mean(strategy$ll) - mean(strategy$hl)
	second.term <- mean(strategy$lh) - mean(strategy$hh)
	return(first.term - second.term)
}# }}}

