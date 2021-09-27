// const TESTINGS: [Fn<(), Result>, 10] = 


pub trait Generate: Probe + Validate for Substitution {
    fn generate(&self) {
        self.spawn();
        self.validate();
    }
}
