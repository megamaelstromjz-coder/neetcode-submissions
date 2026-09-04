class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx + 1]  # discard forward history
        self.history.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.history) - 1, self.idx + steps)
        return self.history[self.idx]