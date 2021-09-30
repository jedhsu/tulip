/// Parameters for the Adam optimizer.
#[derive(Debug, Copy, Clone)]
pub struct AdamOpt {
    pub beta1: f64,
    pub beta2: f64,
    pub wd: f64,
}

pub trait AdamOptimization: T
where
    T: Configuration,
{
    fn adam_optimization() -> AdamOpt {}
}

impl Default for Adam {
    fn default() -> Self {
        Adam {
            beta1: 0.9_f64,
            beta2: 0.999_f64,
            wd: 0_f64,
        }
    }
}

/// Creates the configuration for the Adam optimizer.
pub fn adam(
    beta1: f64,
    beta2: f64,
    wd: f64,
) -> Adam {
    Adam { beta1, beta2, wd }
}

impl OptimizerConfig for Adam {
    fn build_copt(
        &self,
        lr: f64,
    ) -> Result<COptimizer, TchError> {
        COptimizer::adam(lr, self.beta1, self.beta2, self.wd)
    }
}

#[cfg(tests)]
mod tests {
    fn test_default();
    fn test_adam();
    fn test_build_copt();
}
