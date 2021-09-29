use self::super::build;
use self::super::generate;

pub trait Generate: Build + Validate {
    fn generate(&self) {
        self.spawn();
        self.validate();
    }
}
