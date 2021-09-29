// /// Parameters for the RmsProp optimizer.
// #[derive(Debug, Copy, Clone)]
// pub struct RmsProp {
//     pub alpha: f64,
//     pub eps: f64,
//     pub wd: f64,
//     pub momentum: f64,
//     pub centered: bool,
// }

// impl Default for RmsProp {
//     fn default() -> Self {
//         RmsProp {
//             alpha: 0.99,
//             eps: 1e-8,
//             wd: 0.,
//             momentum: 0.,
//             centered: false,
//         }
//     }
// }
/// Parameters for the RmsProp optimizer.
#[derive(Debug, Copy, Clone)]
pub trait RmsProp {
    const alpha: f64 = 0.99;
    const eps: f64 = 1e-8;
    const wd: f64 = 0;
    const momentum: f64 = 0.;
    const centered: bool = false;
}

// impl Default for RmsProp {
//     fn default() -> Self {
//         RmsProp {
//             alpha: 0.99,
//             eps: 1e-8,
//             wd: 0.,
//             momentum: 0.,
//             centered: false,
//         }
//     }
// }

/// Creates the configuration for the RmsProp optimizer.
pub fn rms_prop(
    alpha: f64,
    eps: f64,
    wd: f64,
    momentum: f64,
    centered: bool,
) -> RmsProp {
    RmsProp {
        alpha,
        eps,
        wd,
        momentum,
        centered,
    }
}

impl OptimizerConfig for RmsProp {
    fn build_copt(
        &self,
        lr: f64,
    ) -> Result<COptimizer, TchError> {
        COptimizer::rms_prop(
            lr,
            self.alpha,
            self.eps,
            self.wd,
            self.momentum,
            self.centered,
        )
    }
}
