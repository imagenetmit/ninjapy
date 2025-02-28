"""OAuth2 client credentials flow implementation for NinjaOne."""

from datetime import datetime, timedelta
import httpx
from typing import Optional

class OAuth2ClientCredentials:
    def __init__(
        self,
        token_url: str,
        client_id: str,
        client_secret: str,
        scope: str = "",  # Add scope parameter
    ):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self._access_token: Optional[str] = None
        self._expires_at: Optional[datetime] = None

    async def get_token(self) -> str:
        """Get a valid access token, refreshing if necessary."""
        if not self._is_token_valid():
            await self._refresh_token()
        return self._access_token or ""

    def _is_token_valid(self) -> bool:
        """Check if the current token is valid and not expired."""
        if not self._access_token or not self._expires_at:
            return False
        # Add buffer time of 5 minutes before expiration
        return datetime.utcnow() < (self._expires_at - timedelta(minutes=5))

    async def _refresh_token(self) -> None:
        """Get a new access token using client credentials flow."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.token_url,
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "scope": self.scope,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            data = response.json()
            
            self._access_token = data["access_token"]
            # Calculate expiration time (default to 1 hour if not provided)
            expires_in = int(data.get("expires_in", 3600))
            self._expires_at = datetime.utcnow() + timedelta(seconds=expires_in) 