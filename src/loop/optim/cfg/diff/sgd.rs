/// Parameters for the SGD optimizer.
#[derive(Debug, Copy, Clone)]
pub struct Sgd {
    pub momentum: f64,
    pub dampening: f64,
    pub wd: f64,
    pub nesterov: bool,
}

impl Default for Sgd {
    fn default() -> Self {
        Sgd {
            momentum: 0f64,
            dampening: 0f64,
            wd: 0f64,
            nesterov: false,
        }
    }
}

pub fn sgd(
    momentum: f64,
    dampening: f64,
    wd: f64,
    nesterov: bool,
) -> Sgd {
    Sgd {
        momentum,
        dampening,
        wd,
        nesterov,
    }
}

impl OptimizerConfig for Sgd {
    fn build_copt(
        &self,
        lr: f64,
    ) -> Result<COptimizer, TchError> {
        COptimizer::sgd(
            lr,
            self.momentum,
            self.dampening,
            self.wd,
            self.nesterov,
        )
    }
}
