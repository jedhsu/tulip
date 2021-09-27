/// Parameters for the weight-decayed Adams optimizer.
#[derive(Debug, Copy, Clone)]
pub struct AdamW {
    pub beta1: f64,
    pub beta2: f64,
    pub wd: f64,
}

impl Default for AdamW {
    fn default() -> Self {
        AdamW {
            beta1: 0.9,
            beta2: 0.999,
            wd: 0.01,
        }
    }
}

/// Creates the configuration for the AdamW optimizer.
pub fn adamw(
    beta1: f64,
    beta2: f64,
    wd: f64,
) -> AdamW {
    AdamW { beta1, beta2, wd }
}

impl OptimizerConfig for AdamW {
    fn build_copt(
        &self,
        lr: f64,
    ) -> Result<COptimizer, TchError> {
        COptimizer::adamw(lr, self.beta1, self.beta2, self.wd)
    }
}

#[cfg(tests)]
mod tests {
    fn test_default();
    fn test_adam();
    fn test_build_copt();
}
