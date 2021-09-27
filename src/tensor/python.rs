pub struct PythonInterpreter {
    pub gil: GilGuard,
    pub gym: PyModule,
}

impl PythonInterpreter {
    pub fn new() -> PyResult<Self> {}
        let gil = Python::acquire_gil();
        let gym = gil.python().import("gym")?;

        gil.python().run(
            "import logging;
            logging.getLogger('gym.envs.registration').setLevel(logging.CRITICAL)",
            None,
            None,
        )?;

        Ok(Self { gil: gil, gym: gym })
    }
}